from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

#from config.urls import local_app_urlpatterns
#from django.conf.urls import local_app_urlpatterns

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'default': reverse("api:default:v1_root", request=request, format=format)
    })
    '''
    #import pdb;pdb.set_trace()
    view_url_dict = {}
    namespaces = []
    for local_app_urlpattern in local_app_urlpatterns:
        local_app_namespace = local_app_urlpattern.namespace
        if local_app_namespace == "api":
            namespaces.append(local_app_namespace)
            for versioning_api_urlpattern in local_app_urlpattern.urlpatterns:
                versioning_api_namespaces = namespaces
                version_name = versioning_api_urlpattern.namespace
                versioning_api_namespaces.append(version_name)
                viewname = ':'.join(versioning_api_namespaces)
                view_url_dict[version_name] = reverse(viewname, request=request, format=format)

    return Response(view_url_dict)
    '''
