from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Enbuck(models.Model):

    user = models.ForeignKey(User)
    entime = models.DateTimeField(null=True, blank=True)
    envalue = models.DecimalField(max_digits=12, decimal_places=4)  
    
    def __unicode__(self,):
        return str(self.user)+str(self.entime)