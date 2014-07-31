from django.contrib import admin
from .models import InternalMail

# Register your models here.
class InternalMailAdmin(admin.ModelAdmin):
    class Meta:
        model = InternalMail
        
admin.site.register(InternalMail, InternalMailAdmin)