from django.contrib import admin
from trainreq.models import Lex, Document, Requirement, Verification
from model_utils.models import TimeStampedModel

class LexAdmin(admin.ModelAdmin):
    list_display = ['description','created','modified','document','lex_type','id']
    readonly_fields = ('created', 'modified')
    def get_queryset(self, request):
        qs = Lex.objects.select_subclasses()
        return qs
        
class ReqAdmin(admin.ModelAdmin):
    list_display = ['description','created','modified', 'id']
    readonly_fields = ('created', 'modified')

class VerAdmin(admin.ModelAdmin):
    list_display = ['description','created','modified', 'id']
    readonly_fields = ('created', 'modified')

admin.site.register(Lex, LexAdmin)
admin.site.register(Requirement, ReqAdmin)
admin.site.register(Verification, VerAdmin)

admin.site.register(Document)
    