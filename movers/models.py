from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_driver = models.BooleanField('driver status', default=False)
    is_mover = models.BooleanField('mover status', default=False)

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    middle_name = models.CharField(max_length=255,blank=True, null=True)
    dob = models.CharField(max_length=50,blank=True, null=True)
    gender = models.CharField(max_length=50,blank=True, null=True)
    phone_number = models.CharField(max_length=255,blank=True, null=True)
    full_name=models.CharField(max_length=455, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.full_name = self.user.first_name + ' ' + self.middle_name + ' ' + self.user.last_name
        super().save(*args, **kwargs)