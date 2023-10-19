from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_driver = models.BooleanField('driver status', default=False)
    is_mover = models.BooleanField('mover status', default=False)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class BaseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=455, blank=True, null=True)
    password= models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        middle = " " + self.middle_name if self.middle_name else ""
        self.full_name = f"{self.user.first_name}{middle} {self.user.last_name}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.full_name

class Driver(BaseProfile):
    pass

class Mover(BaseProfile):
    pass

class Profile(models.Model):
    profile_photo = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return str(self.status)

class Vehicle(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(Mover, on_delete=models.CASCADE, null=True, related_name='vehicle')
    plate_number = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    
class MoveRequest(models.Model):
    items = models.CharField(max_length=255, blank=True, null=True)
    destination = models.CharField(max_length=275, blank=True, null=True)
    from_location = models.CharField(max_length=255, blank=True, null=True)
    distance = models.CharField(max_length=255, blank=True, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='move_requests')

    def __str__(self):
        return str(self.items)


class Schedule(models.Model):
    items = models.CharField(max_length=255, blank=True, null=True)
    destination = models.CharField(max_length=275, blank=True, null=True)
    from_location = models.CharField(max_length=255, blank=True, null=True)
    distance = models.CharField(max_length=255, blank=True, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moverequest')

    def __str__(self):
        return str(self.items)