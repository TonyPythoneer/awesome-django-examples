#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2016
#  @date          2016
"""User
"""
import hashlib
from datetime import datetime

from rest_framework import serializers

from pymongo import IndexModel, ASCENDING, DESCENDING

from mongo_connector.connector import db



def _hashed_password(password):
    return hashlib.sha1(password).hexdigest()


class User(serializers.Serializer):
    """User"""
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    updated_at = serializers.DateTimeField(default=datetime.utcnow())

    '''
    INDEXES = db.User.create_indexes([
        IndexModel([("username", ASCENDING)], unique=True),
    ])
    '''
    MODEL = db.User

    def save(self, *args, **kwargs):
        data = self.validated_data

    def set_password(self, password):
        self.validated_data["password"] = _hashed_password(password)

    def create_user(self, username, email, password):
        # Data process: populating the serializer and validate data
        super(User, self).__init__(data={
            "username": username,
            "email": email,
            "password": password,
        })
        self.is_valid()

        # FUCK: 999
        print "fuck"
        self.set_password(password)
        obj_id = self.MODEL.insert_one(self.validated_data)
        return obj_id
