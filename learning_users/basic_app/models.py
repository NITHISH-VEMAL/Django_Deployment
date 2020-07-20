from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)  #inherit from user call where first name last name is automatically imported


    #additional classs
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)   #profile pics folder in media

    def __str__(self):
        return self.user.username
