from django.db import models
from treebeard.mp_tree import MP_Node
from model_utils.models import TimeStampedModel
from django.db.models.signals import pre_save


class Lex(TimeStampedModel):
    """ class to hold a 'lex' which is just a single line in a document: a requirement, """
    """ a verification, etc. """

    reqtype = models.CharField(max_length=50, default=None)
    content = models.CharField(max_length=500)
    created_by = models.ForeignKey('auth.User', related_name='lexs', null=True)

    def parent(self):
        p = self.docthing.get_parent()
        if p is None:
            return None
        else:
            return p.lex.pk
            
    def __unicode__(self):
        return self.content[:20] + (self.content[20:] and '...')
        
    def was_modified_recently(self):
        return self.modified >= timezone.now() - datetime.timedelta(days=1)
        
    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)
        
    # set my own type - this lets us keep a general idea of a 'lex' but give subclasses their
    # own views
    def save(self, *args, **kwargs):
        if self.pk==None:
            self.reqtype=self.__class__.__name__
        super(Lex, self).save(*args, **kwargs)

    # call this when creating a new lex to create a node
    # pass in a lex to make it the parent
    @staticmethod
    def create_docthing(instance, parent=None):
        if parent is None:
            docthing = DocThing.add_root(lex=instance)
            docthing.save()
        else:
            p = parent.docthing
            p.add_child(lex=instance)
            p.save()
    
class Document(Lex):
    """ Class to hold a Document """
    pass

class Category(Lex):
    """ Class to hold a category within a document. Documents can have several of these; every """
    """ document gets one automatically on creation to hold otherwise uncategorized lex's. """
    pass

class DocumentLine(Lex):
    """ Class to represent a requirement, verification test, todo - anything in document content """
    associated = models.ManyToManyField('self')
    
    class Meta:
        abstract = True


class Requirement(DocumentLine):
    """ Class to hold a Requirement """
    pass

class Verification(DocumentLine):
    """ Class to hold a Verification Test """
    pass
    
    
###
#
# Classes for maintaining the document hierarchy
#
###    
    
class DocThing(MP_Node):
    """ Governs the hierarchy of the document tree and lex objects """
    lex = models.OneToOneField(Lex, primary_key=True)

#     def get_annotated_children_list(self):
#         """ get the annotated list of children, not including this node """
#         list = self.get_annotated_list(self)
#         list = list[1:]
#         if list:
#             list[-1][1]['close'].pop()
#         return list
                        
    