from django.db import models, transaction
import os
from django.utils import timezone

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    level = models.CharField(null=True,max_length=10)
    house_no = models.CharField(null=True,max_length=50)
    street_name = models.CharField(null=False,max_length=100)
    area_name = models.CharField(null=False,max_length=100)
    postal_code = models.IntegerField()
    district = models.CharField(max_length=100)
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return str(self.location_id)

# class Admin(AbstractUser):
#     username = models.CharField(blank=True, null=True,max_length=50)
#     email = models.EmailField(_('email address'), unique=True)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
#
#     def __str__(self):
#         return "{}".format(self.email)



# class User(models.Model):
#     user_id=models.IntegerField(primary_key=True)
#     user_name=models.CharField(max_length=50,null=True,blank=True)
#     #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
#     facebook_access_token=models.CharField(max_length=255,unique=True)
#     # user_name=models.CharField(unique=True,max_length=100)
#     # password=models.CharField(max_length=32)
#     first_name=models.CharField(max_length=100,null=True, blank=True)
#     last_name=models.CharField(max_length=100,null=True, blank=True)
#     location_id=models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
#     contact_no=models.IntegerField()
#     email=models.CharField(max_length=100,null=True, blank=True)
#     profile_image=models.ImageField(upload_to='uploads/user/', verbose_name='image',null=True, blank=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#
#     USERNAME_FIELD = 'user_name'
#     REQUIRED_FIELDS = ['facebook_access_token']
#
#     def __str__(self):
#         return self.facebook_access_token