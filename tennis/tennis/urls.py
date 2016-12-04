# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tennis.src.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tennis.views.home', name='home'),
    # url(r'^tennis/', include('tennis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login),
    url(r'^index$', index),
)
