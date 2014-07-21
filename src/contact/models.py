from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    organization = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    
    def __unicode__(self,):
        return "Message from: " + str(self.organization)+" Email: "+str(self.email)