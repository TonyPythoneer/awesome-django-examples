#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2016
#  @date          2016
'''User
'''
import hashlib
from datetime import datetime

from pymongo import IndexModel, ASCENDING, DESCENDING

from mongo_connector.connector import db
from mongo_connector.documents import Document


class User(Document):
    # FIELDS
    _id = None
    username = None
    email = None
    password = None
    updated_at = None

    # manager
    objects = db.User

    # meta
    # fieldname and default as a pair
    FIELDS = {
        "_id": None,
        "username": None,
        "email": None,
        "updated_at": datetime.utcnow,
    }
    '''
    INDEXES = db.User.create_indexes([
        IndexModel([("username", ASCENDING), ("email", ASCENDING)], unique=True),
    ])
    '''

    def __repr__(self):
        tmpl = "<User(username='%s', email='%s')>"
        args = (self.username, self.email)
        return tmpl % args

    def set_password(self, password):
        '''set password'''
        self.password = hashlib.sha1(password).hexdigest()

    @classmethod
    def create_user(cls, username, email, password):
        '''create user'''
        # Data process: populating the serializer and validate data
        model = cls(username=username, email=email, password=password)
        model.set_password(password)
        model.identity = model.objects.insert_one(model.data).inserted_id
        return model
