###
#
# Contains models for the trainreq app
#
# ao 20150210
#
###
import datetime

from django.db import models
from django.db.models.signals import post_init

from django.utils import timezone
from model_utils.managers import InheritanceManager
from model_utils.models import TimeStampedModel

class Document(models.Model):
    """ class to hold documents """
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title

    def get_default_category(self):
        c = Category.objects.filter(document = self)
        return c[0]

def make_new_document(title):
    d = Document(title = title)
    d.save()
    c = Category(description='Uncategorized', document=d)
    c.save()

###
#
# class to hold a 'lex' which is just a single line in a document: a requirement, a verification, etc.
#
###
class Lex(TimeStampedModel):
    """ class to hold a 'lex' which is just a single line in a document: a requirement, """
    """ a verification, etc. """

    description = models.CharField(max_length=200)
    parent = models.ManyToManyField('self',symmetrical=False,blank=True)
    document = models.ForeignKey(Document, null=True)
    objects = InheritanceManager()

    def __unicode__(self):
        return self.description
        
    def was_modified_recently(self):
        return self.modified >= timezone.now() - datetime.timedelta(days=1)
        
    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)
        
    def lex_type(self):
        return self.__class__.__name__

class Requirement(Lex):
    """ Class to hold a Requirement """
    pass

class Verification(Lex):
    """ Class to hold a Verification Test """
    pass

class Category(Lex):
    """ Class to hold a category within a document. Documents can have several of these; every """
    """ document gets one automatically on creation to hold otherwise uncategorized lex's. """
    pass
    
def make_new_lex(type = Requirement, description = None, document = None):
    l = type(description=description, document=document)
    c = document.get_default_category()
    l.save()
    l.parent.add(c)
    return l
        
    