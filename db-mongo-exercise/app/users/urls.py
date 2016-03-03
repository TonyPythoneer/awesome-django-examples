#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2016
#  @date          2016
"""urls: v1_urls
"""
from django.conf.urls import url
from .views import auth


urlpatterns = [
    url(r'^signup$', auth.SignUpView.as_view(), name='user-register'),
]
