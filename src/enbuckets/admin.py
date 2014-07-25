from django.contrib import admin

# Register your models here.
from .models import Enbuck


class EnbuckAdmin(admin.ModelAdmin):
    class Meta:
        model = Enbuck
        
admin.site.register(Enbuck, EnbuckAdmin)