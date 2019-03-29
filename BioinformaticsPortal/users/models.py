from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class PortalUserManager(UserManager):
    pass


class PortalUser(AbstractUser):
    objects =  PortalUserManager()
