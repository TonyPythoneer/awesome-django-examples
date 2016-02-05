from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.core.urlresolvers import resolve


@api_view(('GET',))
def version_root(request, format=None):
    """List urls of this directory
    """
    from . import urls
    r = resolve(request.path_info)
    version_root_namespaces = r.namespaces
    view_url_dict = {}
    instance_api_resolvers = urls.instance_api_urlpatterns
    for instance_api_resolver in instance_api_resolvers:
        instance_api_namespaces = version_root_namespaces
        instance_api_namespaces.append(instance_api_resolver.namespace)
        for endpoint_url_pattern in instance_api_resolver.url_patterns:
            endpoint_namespaces = instance_api_namespaces
            endpoint_name = endpoint_url_pattern.name
            endpoint_namespaces.append(endpoint_name)
            viewname = ':'.join(endpoint_namespaces)
            view_url_dict[endpoint_name] = reverse(viewname, request=request, format=format)
    return Response(view_url_dict)
