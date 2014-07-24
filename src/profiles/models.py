from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User)
       
    Initials = models.CharField(max_length=10)
    English_name = models.CharField(max_length=50)
    Chinese_name = models.CharField(max_length=50, null=True, blank=True)
    is_activate = models.BooleanField(default=True)
    Distription = models.CharField(max_length=200, null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Phone_number = models.CharField(max_length=20,null=True, blank = True)


    slug = models.SlugField()
    image = models.ImageField(upload_to='users/images/',null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    
    
    def __unicode__(self,):
        return str(self.user)
    class Meta:
        ordering = ['English_name',]