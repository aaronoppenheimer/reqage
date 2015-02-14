from reqage.models import *
from reqage.serializers import *
from django.http import Http404
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from serializers import UserSerializer
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

###
#
# Template views
#
###
class HomePageView(TemplateView):
    template_name = "reqage/home.html"

class LexDetailView(DetailView):
    model = Lex
    
###
#
# REST UI views
#
###

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class LexList(generics.ListCreateAPIView):
    queryset = Lex.objects.all()
    serializer_class = LexSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class LexDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lex.objects.all()
    serializer_class = LexSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class RequirementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)    
    
class VerificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
