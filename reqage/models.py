from django.db import models
from treebeard.mp_tree import MP_Node
from model_utils.models import TimeStampedModel


class DocThing(MP_Node):
    """ Governs the hierarchy of the document tree and lex objects """
    type = models.CharField(max_length=50)

    def __unicode__(self):
        return 'Class: %s' % self.type

    def get_annotated_children_list(self):
        """ get the annotated list of children, not including this node """
        list = self.get_annotated_list(self)
        list = list[1:]
        if list:
            list[-1][1]['close'].pop()
        return list
                        
class Lex(TimeStampedModel):
    """ class to hold a 'lex' which is just a single line in a document: a requirement, """
    """ a verification, etc. """

    docthing = models.OneToOneField(DocThing, primary_key=True)
    content = models.CharField(max_length=500)
    created_by = models.ForeignKey('auth.User', related_name='lexs', null=True)

    def __unicode__(self):
        return self.content[:20] + (self.content[20:] and '...')
        
    def was_modified_recently(self):
        return self.modified >= timezone.now() - datetime.timedelta(days=1)
        
    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)
        
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

def make_new_document(title):
    """ make and return a new document with the given title """
    print('DEBUG: making new document >{0}<'.format(title))
    docthing = DocThing.add_root(type='Document')
    docthing.save()
    lex = Document(docthing = docthing, content = title)
    lex.save()
    return lex
    
            
def make_new_requirement(content, docthing):
    """ make and return a new document with the given title """
    print('DEBUG: making new requrirement >{0}< of child {1}'.format(content, docthing.lex.content))
    newdocthing = docthing.add_child(type='Requirement')
    newdocthing.save()
    lex = Requirement(docthing =newdocthing, content = content)
    lex.save()
    return lex    