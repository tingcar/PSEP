from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact
        
admin.site.register(Contact, ContactAdmin)