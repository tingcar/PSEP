from django.contrib import admin

# Register your models here.
from .models import Event
# Register your models here.
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event
        
admin.site.register(Event, EventAdmin)