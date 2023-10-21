from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser (AbstractUser):
    #age = models.PositiveIntergerField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)