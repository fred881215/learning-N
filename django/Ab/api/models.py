from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    phone = models.CharField(max_length=10, blank=True)

    class Meta(AbstractUser.Meta):
        pass
