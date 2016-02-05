#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2015
#  @date          2015
"""v1/users/urls
"""
from django.conf.urls import url

from .views import auth, personal, password


urlpatterns = [
    #
    url(r'^register$', auth.SignUpView.as_view(), name='user-register'),
    url(r'^login$', auth.LoginView.as_view(), name='user-login'),
    url(r'^logout$', auth.LogoutView.as_view(), name='user-logout'),
    #
    url(r'^me$', personal.AboutMeView.as_view(), name='user-me'),
    url(r'^(?P<pk>[0-9]+)$', personal.UserDetailView.as_view(), name='user-detail'),
    #
    url(r'^password_change$', password.PasswordChangeView.as_view(), name='user-password-change'),
]
