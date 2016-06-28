from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list_task, name='panel_lista'),
    url (r'^panel/(?P<pk>[0-9]+)/$', views.panel_detail, name='panel_detalle'),
    url(r'^panel/new/$', views.panel_new, name='panel_new'),
]