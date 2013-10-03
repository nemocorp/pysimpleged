# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^$', 'app.views.test_cmd'),
    (r'^all$', 'app.views.all'),
    (r'^add$', 'app.views.add'),
)
