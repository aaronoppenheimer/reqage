from django.conf.urls import patterns, url

from reqage import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^document/(?P<document_id>\d+)/$', views.document, name='document'),
    url(r'^lex/(?P<lex_id>\d+)/$', views.lex, name='lex'),
    url(r'^newdocument/$', views.newdocument, name='newdocument'),    
    url(r'^newlex/$', views.newlex, name='newlex'),    
#     url(r'^addparentlex/$', views.addparentlex, name='addparentlex'),    
)