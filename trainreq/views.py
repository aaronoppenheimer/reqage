from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

import trainreq.models as models
from trainreq.models import Document, Lex, Requirement, Verification

######
#
# Main View
#
######

def index(request):
    document_list = Document.objects.all()    
    context = { 'document_list': document_list }
    return render(request, 'trainreq/index.html', context)

def newdocument(request):
    if request.method == 'GET':
        return render(request, 'trainreq/newdocument.html')
    else: # request.method == 'POST':
        if 'title' in request.POST:
            t = request.POST['title'].strip()
            if len(t)==0:
                return render(request, 'trainreq/newdocument.html', {'error_message':'title must have length > 0'})
            else:
                d = models.make_new_document(title=request.POST['title'])
                return HttpResponseRedirect(reverse('trainreq:index'))
        else:
            return render(request, 'trainreq/newdocument.html')

######
#
# Document Views
#
######

def document(request, document_id):
    if request.method == 'GET':
        try:
            doc = Document.objects.get(pk=document_id)
        except Document.DoesNotExist:
            raise Http404("Document does not exist")
        lex_list = Lex.objects.filter(document=doc).select_subclasses()
        return render(request, 'trainreq/document.html', {'document': doc,
                                                          'lex_list': lex_list})
    else:
        return HttpResponseRedirect(reverse('trainreq:index'))        
        
######
#
# Lex Views
#
######

def lex(request, lex_id):
    try:
        item = Lex.objects.get_subclass(pk=lex_id)
    except Document.DoesNotExist:
        raise Http404("Document does not exist")
    lex_type = item.__class__.__name__.lower()
    children_list = Lex.objects.filter(parent=item).select_subclasses()
    parent_list = item.parent.all()
    return render(request, 'trainreq/{0}.html'.format(lex_type), {'item': item,
                                                         'parents': parent_list,
                                                         'children': children_list})

def newlex(request):
    if request.method == 'GET':
        document_id = request.GET.get('docid', None)
        return render(request, 'trainreq/newlex.html', {'docid': document_id})
    else: # request.method == 'POST':
        if 'description' not in request.POST or request.POST['description'].strip()=='':
            return render(request, 'trainreq/newlex.html', {'error_message':'title must have length > 0'})
        d = request.POST['description'].strip()
        
        if 'docid' not in request.POST or request.POST['docid'].strip()=='':
            return render(request, 'trainreq/newlex.html', {'error_message':'need a document'})
        doc = Document.objects.get(id=request.POST['docid'].strip())
        
        models.make_new_lex(description = d, document = doc)
        return HttpResponseRedirect(reverse('trainreq:document', args=(doc.id,)))

def addparentlex(request):
    if request.method == 'POST':
        newparent_id = request.POST.get('newparent','')
        childlex_id = request.POST.get('childlex','')
        childlex_id = int(childlex_id)
        childlex = Lex.objects.get_subclass(id=childlex_id)
        if newparent_id == '':
            return render(request, 'trainreq/{0}.html'.format(childlex.lex_type()), {'error_message':'must have a parent'})            
        else:
            newparent_id = int(newparent_id)
            childlex.parent.add(newparent_id)
            return lex(request, lex_id = childlex.id)
    else:
        pass # what do do?        