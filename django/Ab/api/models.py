from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    phone = models.CharField(max_length=10, blank=True)

    class Meta(AbstractUser.Meta):
        pass

class UserSet(models.Model):
    uid = models.CharField(max_length = 100,blank=True)
    name  = models.CharField(max_length=20,blank=True)
    birthday  = models.CharField(max_length=20,blank=True)
    height  = models.CharField(max_length=20,blank=True)
    gender  = models.CharField(max_length=20,blank=True)
    fcm_id  = models.CharField(max_length=20,blank=True)
    address  = models.CharField(max_length=20,blank=True)
    weight  = models.CharField(max_length=20,blank=True)
    phone  = models.CharField(max_length=20,blank=True)
    email  = models.CharField(max_length=20,blank=True)
    def __str__(self):
        data = dict()
        data = {
            'name':self.name,
            'birthday':self.birthday,
            'height':self.height,
            'gender':self.gender,
            'fcm_id':self.fcm_id,
            'address':self.address,
            'weight':self.weight,
            'phone':self.phone,
            'email':self.email
        }
        return str(data)