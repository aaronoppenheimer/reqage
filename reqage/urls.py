from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from reqage import views

urlpatterns = patterns('',
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^documents/$', views.DocumentList.as_view()),
    url(r'^documents/(?P<pk>[0-9]+)/$', views.DocumentDetail.as_view()),
#     url(r'^$', views.index, name='index'),
#     url(r'^document/(?P<document_id>\d+)/$', views.document, name='document'),
#     url(r'^lex/(?P<lex_id>\d+)/$', views.lex, name='lex'),
#     url(r'^newdocument/$', views.newdocument, name='newdocument'),    
#     url(r'^newlex/$', views.newlex, name='newlex'),    
# #     url(r'^addparentlex/$', views.addparentlex, name='addparentlex'),    
)

urlpatterns = format_suffix_patterns(urlpatterns)