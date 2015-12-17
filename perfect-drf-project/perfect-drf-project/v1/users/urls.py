#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2015
#  @date          2015
"""v1/users/urls
"""
from django.conf.urls import patterns, url

from .views import auth, personal


urlpatterns = [
    #
    url(r'^register$', auth.SignUpView.as_view(), name='user-register'),
    url(r'^login$', auth.LoginView.as_view(), name='user-login'),
    url(r'^logout$', auth.LogoutView.as_view(), name='user-logout'),
    #
    url(r'^me$', personal.AboutMeView.as_view(), name='user-me'),
    url(r'^(?P<pk>[0-9]+)$', personal.UserDetailView.as_view(), name='user-detail'),
]


'''
router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
'''

'''
from .views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

urlpatterns = patterns(
    '',
    # URLs that do not require a session or valid token
    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
)
'''
