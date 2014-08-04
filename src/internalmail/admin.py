from django.contrib import admin
from .models import InternalMail, OutMail

# Register your models here.
class InternalMailAdmin(admin.ModelAdmin):
    class Meta:
        model = InternalMail
        
admin.site.register(InternalMail, InternalMailAdmin)

class OutMailAdmin(admin.ModelAdmin):
    class Meta:
        model = OutMail
        
admin.site.register(OutMail, OutMailAdmin)