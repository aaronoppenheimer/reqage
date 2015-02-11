from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.apps import apps

from reqage.models import *

######
#
# Main View
#
######

def index(request):
    document_list = DocThing.get_root_nodes()    
    context = { 'document_list': document_list }
    return render(request, 'reqage/index.html', context)

def newdocument(request):
    if request.method == 'GET':
        return render(request, 'reqage/newdocument.html')
    else: # request.method == 'POST':
        if 'title' in request.POST:
            t = request.POST['title'].strip()
            if len(t)==0:
                return render(request, 'reqage/newdocument.html', {'error_message':'title must have length > 0'})
            else:
                d = models.make_new_document(title=request.POST['title'])
                return HttpResponseRedirect(reverse('reqage:index'))
        else:
            return render(request, 'reqage/newdocument.html')

######
#
# Document Views
#
######

def document(request, document_id):
    if request.method == 'GET':
        try:
            doc = DocThing.objects.get(pk=document_id)
        except Document.DoesNotExist:
            raise Http404("Document does not exist")
        annotated_list = DocThing.get_annotated_list(doc)
        return render(request, 'reqage/document.html', {'document': doc,
                                                          'annotated_list': annotated_list[1:]})
    else:
        return HttpResponseRedirect(reverse('reqage:index'))        
        
######
#
# Lex Views
#
######

def lex(request, lex_id):
    try:
        docthing = DocThing.objects.get(pk=lex_id)
    except Document.DoesNotExist:
        raise Http404("Document does not exist")
    lex_type = docthing.type
    parent = docthing.get_parent()
    children = docthing.get_annotated_children_list()
    
    # now get the content itself
    item_class = apps.get_model(app_label='reqage', model_name=lex_type)
    item = docthing.lex
    item.__class__ = item_class
    
    # now get the document we're in
    item_doc = docthing.get_root()
    
    return render(request, 'reqage/{0}.html'.format(lex_type), {'item': item,
                                                                'document': item_doc,
                                                                'parent': parent,
                                                                'children_annotated_list': children})
# 
# def newlex(request):
#     if request.method == 'GET':
#         document_id = request.GET.get('docid', None)
#         return render(request, 'trainreq/newlex.html', {'docid': document_id})
#     else: # request.method == 'POST':
#         if 'description' not in request.POST or request.POST['description'].strip()=='':
#             return render(request, 'trainreq/newlex.html', {'error_message':'title must have length > 0'})
#         d = request.POST['description'].strip()
#         
#         if 'docid' not in request.POST or request.POST['docid'].strip()=='':
#             return render(request, 'trainreq/newlex.html', {'error_message':'need a document'})
#         doc = Document.objects.get(id=request.POST['docid'].strip())
#         
#         models.make_new_lex(description = d, document = doc)
#         return HttpResponseRedirect(reverse('trainreq:document', args=(doc.id,)))
# 
# def addparentlex(request):
#     if request.method == 'POST':
#         newparent_id = request.POST.get('newparent','')
#         childlex_id = request.POST.get('childlex','')
#         childlex_id = int(childlex_id)
#         childlex = Lex.objects.get_subclass(id=childlex_id)
#         if newparent_id == '':
#             return render(request, 'trainreq/{0}.html'.format(childlex.lex_type()), {'error_message':'must have a parent'})            
#         else:
#             newparent_id = int(newparent_id)
#             childlex.parent.add(newparent_id)
#             return lex(request, lex_id = childlex.id)
#     else:
#         pass # what do do?        