"""myproject URL Configuration

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
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^HomePrayer/', include('HomePrayer.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', 'views.home'),
    url(r'^logout/$', 'views.logout'),
    url(r'^done/$', 'views.done', name='done'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', 'views.ajax_auth',
        name='ajax-auth'),
    url(r'^email/$', 'views.require_email', name='require_email'),
]
