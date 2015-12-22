#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2015
#  @date          2015
"""users/serializers/personal
"""
from django.contrib.auth import get_user_model
#from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.reverse import reverse


# Get the UserModel
User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class AboutMeSerializer(serializers.ModelSerializer):
    user_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'user_url')

    def get_user_url(self, obj):
        return reverse(
            'api:default:users:user-detail',
            kwargs={'pk': obj.pk},
        )

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.email)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        return instance
