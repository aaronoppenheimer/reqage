from django.conf.urls import patterns, include, url
from django.contrib import admin
import rest_framework

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^trainreq/', include('trainreq.urls', namespace='trainreq', app_name='trainreq')),
    url(r'^reqage/', include('reqage.urls', namespace='reqage', app_name='reqage')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
