from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):

    name = models.CharField('name', max_length=15, blank=False, null=False)

    password = models.CharField('password', blank=False, null=False, max_length=250)

    email = models.EmailField('email', max_length=50, blank=False, null=False)

    token = models.CharField('token', blank=False, null=False, max_length=500)

    token_expires = models.DateTimeField('token_expires', blank=True, null=True)

    created_at =  models.DateTimeField('created_at',  default = timezone.now)

    def __str__(self):
        return self.name 


