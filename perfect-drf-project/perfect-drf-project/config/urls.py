"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url


versioning_api_urlpatterns = [
    url(r'', include('v1.urls', namespace='default')),  # Default versioning api url
    url(r'^v1/', include('v1.urls', namespace='v1')),  # Versioning api url
]

third_party_urlpatterns = [
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

local_app_urlpatterns = [
    url(r'^api/', include(versioning_api_urlpatterns, namespace='api')),
    url(r'^$', include('api_root.urls', namespace='api_root')),
]

urlpatterns = local_app_urlpatterns + third_party_urlpatterns
