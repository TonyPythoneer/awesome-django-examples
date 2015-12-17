#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2015
#  @date          2015
"""users/serializers/auth
"""
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token


# Get the UserModel
User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def save(self, *args, **kwargs):
        """create user
        """
        User.objects.create_user(**self.validated_data)

    def to_representation(self, obj):
        """Delete important info, for instance, password
        """
        ret = super(SignUpSerializer, self).to_representation(obj)
        ret.pop("password", None)
        return ret


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, username, password):
        # Authentication through username
        if username and password:
            self.user = authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg)

    def user_exists_or_not(self):
        # Did we get back an active user?
        if not self.user:
            msg = _('Incorrect username or password.')
            raise serializers.ValidationError(msg)

    def user_is_active_or_not(self):
        if not self.user.is_active:
            msg = _('User account is disabled.')
            raise serializers.ValidationError(msg)

    def get_user(self):
        return self.user

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        self.authenticate(username, password)
        self.user_exists_or_not()
        self.user_is_active_or_not()

        attrs['user'] = self.get_user()
        return attrs


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = Token
        fields = ('key',)
