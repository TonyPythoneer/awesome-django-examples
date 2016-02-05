#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2015
#  @date          2015
"""users/views/auth
"""
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from api_root.authentications.auth import ExpiringTokenAuthentication
from ..serializers.auth import SignUpSerializer, LoginSerializer, TokenSerializer


User = get_user_model()


class SignUpView(generics.CreateAPIView):
    """
    """
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save()


class LoginView(generics.CreateAPIView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework
    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    token_model = Token
    response_serializer = TokenSerializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.token, created = self.token_model.objects.get_or_create(user=self.user)
        #login(self.request, self.user)

    def get_response(self):
        token_data = self.response_serializer(self.token).data
        return Response(token_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        self.login()
        return self.get_response()


class LogoutView(generics.DestroyAPIView):
    """
    Calls Django logout method and delete the Token object
    assigned to the current User object.
    Accepts/Returns nothing.
    """
    authentication_classes = (ExpiringTokenAuthentication,)
    permission_classes = (AllowAny,)

    def delete(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        #logout(request)

        return Response({'fuck': 123}, status=status.HTTP_204_NO_CONTENT)
