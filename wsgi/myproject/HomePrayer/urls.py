from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^addPrayer/$', views.addPrayer, name='addPrayer'),
    url(r'^login/$', 'views.home'),
    url(r'^logout/$', 'views.logout'),
    url(r'^done/$', 'views.done', name='done'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', 'views.ajax_auth',
        name='ajax-auth'),
    url(r'^email/$', 'views.require_email', name='require_email'),
]
