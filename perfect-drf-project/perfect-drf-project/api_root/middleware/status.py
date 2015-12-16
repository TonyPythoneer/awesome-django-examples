#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20150923
#  @date          20150923
#  @version       0.0 - Finish prototype for middlewares
"""middlewares

.. _Django Document - Middleware - Hooks and application order:
    https://docs.djangoproject.com/en/1.8/topics/http/middleware/#hooks-and-application-order
"""
from rest_framework import status


class StatusMiddleware(object):
    """StatusMiddleware

    """
    def process_response(self, request, response):
        """process_response
        """
        #import pdb; pdb.set_trace();
        if status.is_success(response.status_code):
            response.data['status'] = 'success'
        #import pdb; pdb.set_trace();
        response.data['status'] = 'success'
        print response
        print response.data
        #return super(MessageMiddleware, self).finalize_response(request, response, *args, **kwargs)
        return response
