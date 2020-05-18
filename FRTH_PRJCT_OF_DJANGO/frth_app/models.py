from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class User_Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #ADDING EXTRA ATTRIBUTES OTHER THE USER ALREADY HAS

    port_folio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username
