#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2015
#  @date          2015
"""urls: api_root_urls
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.api_root, name='api_root'),
]
