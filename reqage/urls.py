from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from reqage import views

urlpatterns = patterns('',
    url(r'^$', views.HomePageView.as_view(), name='home'),
# rest api
    url(r'^api/users/$', views.UserList.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api/document/$', views.DocumentList.as_view()),
    url(r'^api/document/(?P<pk>[0-9]+)/$', views.DocumentDetail.as_view()),
    url(r'^api/lex/$', views.LexList.as_view()),
    url(r'^api/lex/(?P<pk>[0-9]+)/$', views.LexDetail.as_view()),
    url(r'^api/requirement/(?P<pk>[0-9]+)/$', views.RequirementDetail.as_view()),
    url(r'^api/verification/(?P<pk>[0-9]+)/$', views.VerificationDetail.as_view()),

# function api
    url(r'^lexdetail/(?P<pk>[0-9]+)/$', views.LexDetailView.as_view()),


#     url(r'^$', views.index, name='index'),
#     url(r'^document/(?P<document_id>\d+)/$', views.document, name='document'),
#     url(r'^lex/(?P<lex_id>\d+)/$', views.lex, name='lex'),
#     url(r'^newdocument/$', views.newdocument, name='newdocument'),    
#     url(r'^newlex/$', views.newlex, name='newlex'),    
# #     url(r'^addparentlex/$', views.addparentlex, name='addparentlex'),    
)

urlpatterns = format_suffix_patterns(urlpatterns)