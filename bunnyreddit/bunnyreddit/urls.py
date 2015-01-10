from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bunnyreddit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'bunnyreddit.views.home', name='home'),
    url(r'^post/(?P<name>[^/]+)[/]?$', 'bunnyreddit.views.getPost' , name='post'),

)
