#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160301
#  @date          20160301
"""client app
Config example:
    URI (str): "mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
        or "mongodb://{HOST}:{PORT}/{DBNAME}"
    HOST (str): "localhost"
    PORT (int): 27017
    DBNAME (str): dbname
    USERNAME (str): username or not
    PASSWORD (str): password or not

MONGODB_CONFIG = {
    'URI': '',
    'HOST': 'localhost',
    'PORT': 27017,
    'DBNAME': 'dbname',
    'USERNAME': '',
    'PASSWORD': '',
}
"""
import sys

from django.conf import settings

from pymongo import MongoClient


try:
    MONGODB_CONFIG = settings.MONGODB_CONFIG
except AttributeError:
    print "It doesn't have MONGODB_CONFIG in settings!"
    sys.exit()


def _get_uri_format(has_auth):
    '''return uri format of string template'''
    if has_auth:
        return "mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
    return "mongodb://{HOST}:{PORT}/{DBNAME}"


class MongoConnector(object):

    def __init__(self):
        self.mongo_config = MONGODB_CONFIG
        self._connect_db()

    def _has_authentication(self):
        '''check authentication if you have offered'''
        user = self.mongo_config.get('USERNAME', '')
        password = self.mongo_config.get('PASSWORD', '')
        return bool(user and password)

    def _has_uri(self):
        '''check uri if you have offered'''
        uri = self.mongo_config.get('URI', '')
        return bool(uri)

    def _get_uri(self):
        '''get uri'''
        if self._has_uri():
            uri = self.mongo_config['URI']
        else:
            # Data process: Set the uri
            has_auth = self._has_authentication()
            uri_format = _get_uri_format(has_auth)
            uri = uri_format.format(**self.mongo_config)
        return uri

    def _connect_db(self):
        '''Making a Connection with MongoClient'''
        uri = self._get_uri()
        self.client = MongoClient(uri)

    def get_db(self):
        '''Getting a Database'''
        db_name = self.mongo_config['DBNAME']
        return self.client[db_name]


connector = MongoConnector()
db = connector.get_db()
