#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2015
#  @date          2015
"""urls: v1_urls
"""
from django.conf.urls import include, url
from .users import urls as user_urls

from . import views

instance_api_urlpatterns = [
    url(r'^users/', include(user_urls, namespace='users')),
]

urlpatterns = instance_api_urlpatterns + [
    url(r'^$', views.version_root, name='v1_root'),
]
