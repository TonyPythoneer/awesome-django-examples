#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2015
#  @date          2015
"""users/views/password
"""
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api_root.authentications.auth import ExpiringTokenAuthentication
from ..serializers.password import PasswordChangeSerializer


class PasswordChangeView(generics.UpdateAPIView):
    """
    Calls Django Auth SetPasswordForm save method.
    Accepts the following PATCH parameters: new_password1, new_password2
    Returns the success/fail message.
    """
    authentication_classes = (ExpiringTokenAuthentication,)
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})
