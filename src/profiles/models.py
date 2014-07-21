from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User)
       
    Initials = models.CharField(max_length=10)
    English_name = models.CharField(max_length=50)
    Chinese_name = models.CharField(max_length=50, null=True, blank=True)
    is_activate = models.BooleanField(default=True)
    Post = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='users/images/',null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    Timeslot1 = models.IntegerField(null=True, default=1)
    Timeslot2 = models.IntegerField(null=True, default=1)
    Timeslot3 = models.IntegerField(null=True, default=1)
    Timeslot4 = models.IntegerField(null=True, default=1)
    
    
    def __unicode__(self,):
        return str(self.user)
    class Meta:
        ordering = ['English_name',]