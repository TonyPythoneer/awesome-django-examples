#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    2015
#  @date          2015
#  @version       0.0 - Finish prototype for middlewares
"""middlewares

.. _Django Document - Middleware - Hooks and application order:
    https://docs.djangoproject.com/en/1.8/topics/http/middleware/#hooks-and-application-order
"""
from rest_framework import status
from rest_framework.response import Response


class RestfulStatusMiddleware(object):
    """RestfulStatusMiddleware

    According to `The Response class extends SimpleTemplateResponse` in
    Response of DRF document, when it sets data in data of response, it
    will trigger to render.

    However, data of attributes of response is `The unrendered content
    of a Request object.`, if it needs to be modified, it has to make
    in process_template_response.
    """
    def process_template_response(self, request, response):
        """process_template_response
        """
        if self.is_rest_framework_response(response):
            if self.is_dict_of_data(response.data):
                #import pdb; pdb.set_trace();
                if status.is_success(response.status_code):
                    response.data['status'] = 'ok'
                    #response.data['status_code'] = response.status_code
                    #response.data['status_text'] = response.status_text
                if status.is_client_error(response.status_code):
                    response.data['status'] = 'error'
        return response

    def is_rest_framework_response(self, response):
        return isinstance(response, Response)

    def is_dict_of_data(self, data):
        return isinstance(data, dict)
