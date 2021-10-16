from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_pic = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def split_biography(self):
        return self.biography.split("\n")
