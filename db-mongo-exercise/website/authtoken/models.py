#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2016
#  @date          2016
'''Token
'''
import binascii
import os

from django.core.exceptions import ObjectDoesNotExist

from pymongo import IndexModel, ASCENDING, DESCENDING

from users.models import User

from mongo_connector.connector import db
from mongo_connector.documents import Document


class Token(Document):
    '''token'''
    # FIELDS
    _id = None
    _user = None
    key = None

    # manager
    objects = db.Token

    # meta
    # fieldname and default as a pair
    FIELDS = {
        "_id": None,
        "_user": None,
        "key": None,
    }
    '''
    INDEXES = db.Token.create_indexes([
        IndexModel([("_user", ASCENDING)], unique=True),
        IndexModel([("key", ASCENDING)], unique=True),
    ])
    '''

    def __init__(self, *args, **kwargs):
        super(Token, self).__init__(*args, **kwargs)
        self.key = self.generate_key()

    def __repr__(self):
        tmpl = "<Token(key='%s', username=%s, email='%s')>"
        user = User.objects.find_one({'_id': self.obj_id(self._user)})
        if not user:
            raise ObjectDoesNotExist
        args = (self.key, user['username'], user['email'])
        return tmpl % args

    @property
    def user(self):
        '''get user'''
        return self.obj_id(self._user)

    @user.setter
    def user(self, doc):
        '''set user'''
        self._user = self.obj_id(doc)

    @staticmethod
    def generate_key():
        '''generate_key'''
        return binascii.hexlify(os.urandom(128)).decode()

    @classmethod
    def create_user(cls, username, email, password):
        '''create user'''
        # Data process: populating the serializer and validate data
        model = cls(username=username, email=email, password=password)
        model.set_password(password)
        model.identity = model.objects.insert_one(model.data).inserted_id
        return model
