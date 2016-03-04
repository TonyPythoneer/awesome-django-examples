#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2016
#  @date          2016
'''Document
'''
from bson.objectid import ObjectId


class Document(object):
    '''Document'''
    # FIELDS
    _id = None

    # manager
    objects = None

    # meta
    FIELDS = None

    '''
    INDEXES = db.User.create_indexes([
        IndexModel([("username", ASCENDING), ("email", ASCENDING)], unique=True),
    ])
    '''

    def __init__(self, **kwargs):
        for key, default in self.FIELDS.items():
            if hasattr(default, '__call__'):
                default = default()
            value = kwargs.get(key, default)
            self.__dict__[key] = value

    def __repr__(self):
        tmpl = "<User(username='%s', email='%s')>"
        args = (self.username, self.email)
        return tmpl % args

    @property
    def identity(self):
        '''return private variable'''
        return self._id

    @identity.setter
    def identity(self, identity):
        '''access private variable'''
        self._id = identity

    @property
    def data(self):
        '''return data'''
        return {key: self.__dict__[key] for key in self.FIELDS if self.__dict__.get(key)}

    @staticmethod
    def obj_id(obj_id):
        '''convert obj_id or not'''
        return obj_id if isinstance(obj_id, ObjectId) else ObjectId(obj_id)
