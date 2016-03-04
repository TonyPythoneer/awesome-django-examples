#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2016
#  @date          2016
"""Serialize model instance
"""
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    '''UserSerializer'''
    _id = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    updated_at = serializers.DateTimeField()
