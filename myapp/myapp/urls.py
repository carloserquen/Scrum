#from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from apps.login.views import *
 
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^tarea/', include('apps.tarea.urls')),
    url(r'^proyecto/', include('apps.proyecto.urls')),
)
