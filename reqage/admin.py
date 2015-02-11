from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from reqage.models import *

class DocThingAdmin(TreeAdmin):
    form = movenodeform_factory(DocThing)
    list_display = ['type','lex','id']

admin.site.register(DocThing,DocThingAdmin)




class LexAdmin(admin.ModelAdmin):
    list_display = ['content','created','modified']
    readonly_fields = ('created', 'modified')
        
class ReqAdmin(admin.ModelAdmin):
    list_display = ['content','created','modified']
    readonly_fields = ('created', 'modified')

class VerAdmin(admin.ModelAdmin):
    list_display = ['content','created','modified']
    readonly_fields = ('created', 'modified')

admin.site.register(Lex, LexAdmin)
admin.site.register(Requirement, ReqAdmin)
admin.site.register(Verification, VerAdmin)
