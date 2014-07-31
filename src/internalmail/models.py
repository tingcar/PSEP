from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class InternalMail(models.Model):
    user = models.ForeignKey(User)
    Ticketid = models.CharField(max_length=50, null=True, blank=True)


    From = models.CharField(max_length=50, null=True, blank=True)
    FromEmail = models.CharField(max_length=50, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    Content = models.CharField(max_length=200, null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    Title = models.CharField(max_length=50, null=True, blank=True)


    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    
    
    def __unicode__(self,):
        return "From: "+str(self.From)+" To: "+str(self.user)+" Title: "+str(self.Title)
    class Meta:
        ordering = ['timestamp',]