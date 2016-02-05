#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20150923
#  @date          20150923
#  @version       0.0 - Finish prototype for middlewares
"""middlewares

.. _Django Document - Middleware - Hooks and application order:
    https://docs.djangoproject.com/en/1.8/topics/http/middleware/#hooks-and-application-order
"""
from django.core.urlresolvers import reverse, resolve, NoReverseMatch
from django.http import Http404


class VersioningAPIMiddleware(object):
    """VersioningAPIMiddleware

    During the request phase, before calling the view, Django applies middleware
    in the order it’s defined in MIDDLEWARE_CLASSES.

    To use `process_request()` to change the path_info for view. Transmit versioning
    url after parsing header and combining path_info.
    """
    def process_request(self, request):
        """process_request

        Whether User directly accesses default or appointed versioning url, it will
        resolve the path_info. And, suppose the request contains version in header,
        it will get from it.

        If header contains version, it will replace the old version by new version,
        recombining a new path_info and transmitting the request.
        """
        # Local variables: There are necessary variables.
        r = resolve(request.path_info)
        version = request.META.get('HTTP_X_API_VERSION', False)

        # Data process: Replace the old version by new version
        if version:
            old_version = r.namespace.split(':')[1]
            '''
            for k,v in request.META.items():
                print k,v
            '''
            new_namespace = r.namespace.replace(old_version, version)
            new_url_name = '{}:{}'.format(new_namespace, r.url_name)
            #print new_url_name
            try:
                request.path_info = reverse(new_url_name, args=r.args, kwargs=r.kwargs)
            except NoReverseMatch:
                raise Http404()
