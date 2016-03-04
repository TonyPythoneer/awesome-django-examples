#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2016
#  @date          2016
"""users/views/auth
"""
from django.db import IntegrityError

from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from pymongo.errors import DuplicateKeyError

from ..serializers.auth import SignUpSerializer
from ..models import User


class SignUpView(generics.CreateAPIView):
    """SignUpView
    """
    model_class = User
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Validation process: Receive request and validate data
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        data = self.serializer.data

        #
        # a = self.model_class.create_user(**data)
        try:
            instance = self.model_class.create_user(**data)
        except DuplicateKeyError as err:
            raise APIException({"fuck": 13})
        print instance.data

        return Response({}, status=status.HTTP_200_OK)
