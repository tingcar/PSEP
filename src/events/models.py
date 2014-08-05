from django.db import models

# Create your models here.
class Event(models.Model):

    title = models.CharField(max_length=50)
    organizer = models.CharField(max_length = 100)
    content = models.CharField(max_length=500)
    iid = models.CharField(max_length=20, null=True, blank=True)
    venue = models.CharField(max_length=100, null=True, blank=True)
    eventtype = models.CharField(max_length=20, null=True, blank=True)

    slug = models.SlugField()
    image = models.ImageField(upload_to='events/images/',null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __unicode__(self,):
        return "Events: " + str(self.title)