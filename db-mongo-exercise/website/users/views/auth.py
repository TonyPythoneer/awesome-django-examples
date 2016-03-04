#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2016
#  @date          2016
"""users/views/auth
"""
from rest_framework import status, generics
from rest_framework.response import Response

from pymongo.errors import DuplicateKeyError

from ..serializers import UserSerializer
from ..req_serializers.auth import SignUpSerializer
from ..models import User
from utils.error_codes import err_users


class SignUpView(generics.CreateAPIView):
    """SignUpView"""
    model_class = User
    model_serializer_class = UserSerializer
    req_serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        # Validation process: Receive request and validate data
        req_serializer = self.req_serializer_class(data=self.request.data)
        req_serializer.is_valid(raise_exception=True)
        data = req_serializer.data
        print data

        # Model process: Ceate new user
        try:
            model = self.model_class.create_user(**data)
        except DuplicateKeyError:
            return Response(err_users.REGISTERED_ACC,
                            status=status.HTTP_400_BAD_REQUEST)

        # Result process: Serialize model
        ret = self.model_serializer_class(model).data

        return Response(ret, status=status.HTTP_200_OK)
