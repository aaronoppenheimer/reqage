from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from reqage.models import *

class DocThingAdmin(TreeAdmin):
    form = movenodeform_factory(DocThing)
    list_display = ['lex']

admin.site.register(DocThing,DocThingAdmin)


class LexAdmin(admin.ModelAdmin):
    list_display = ['content','lextype', 'parent', 'created','modified','pk', 'created_by']
    readonly_fields = ('lextype', 'created', 'modified', 'pk')
        
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['content','created','modified','pk']
    readonly_fields = ('created', 'modified', 'pk')

class RequirementAdmin(admin.ModelAdmin):
    list_display = ['content','created','modified']
    readonly_fields = ('created', 'modified')

class VerificationAdmin(admin.ModelAdmin):
    list_display = ['content','created','modified','complete']
    readonly_fields = ('created', 'modified')

admin.site.register(Lex, LexAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Verification, VerificationAdmin)
