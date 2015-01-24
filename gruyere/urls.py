from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import login, main

urlpatterns = patterns('',
                       url(r'^$', login, name='login'),
                       url(r'^main$', main, name='main'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
