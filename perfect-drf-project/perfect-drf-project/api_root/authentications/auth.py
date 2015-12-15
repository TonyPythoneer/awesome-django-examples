#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2015
#  @date          2015
#  @version       0.0
'''authentications
'''
import datetime

from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.authtoken.models import Token


class ExpiringTokenAuthentication(TokenAuthentication):
    """Add inspecting expired token feature, for the admin's exclusive use.

    Simple token based authentication.
    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:
        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    model = Token
    """
    A custom token model may be used, but must have the following properties.
    * key -- The string identifying the token
    * user -- The user to which the token belongs
    """
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        # Validation process: Don't allow the not containing token
        if not auth or auth[0].lower() != b'token':
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.select_related('user').get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        # Validation process: If The token is over 24 hours, it will delete.
        utc_now = datetime.datetime.utcnow().replace(tzinfo=utc)
        if token.created < utc_now - datetime.timedelta(hours=24):
            token.delete()
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token)
