#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2016
#  @date          2016
"""
"""
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class SignUpView(generics.CreateAPIView):
    """SignUpView
    """
    permission_classes = (AllowAny,)
    #serializer_class = LoginSerializer
    #esponse_serializer = TokenSerializer

    def get_response(self):
        token_data = self.response_serializer(self.token).data
        return Response(token_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print request.data
        '''
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        self.login()
        '''
        return Response({}, status=status.HTTP_200_OK)

