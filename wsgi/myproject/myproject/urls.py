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

admin.autodiscover()

urlpatterns = [
    url(r'^$', 'myproject.app.views.home'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^HomePrayer/', include('HomePrayer.urls')),
    url(r'^email-sent/', 'myproject.app.views.validation_sent'),
    url(r'^login/$', 'myproject.app.views.home'),
    url(r'^logout/$', 'myproject.app.views.logout'),
    url(r'^done/$', 'myproject.app.views.done', name='done'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', 'myproject.app.views.ajax_auth',
        name='ajax-auth'),
    url(r'^email/$', 'myproject.app.views.require_email', name='require_email'),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
]
