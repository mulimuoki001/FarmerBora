from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from PIL import Image


class CustomUser(AbstractUser):
    role = models.CharField(max_length=100)
    profile_picture = models.FileField(
        upload_to="pics", blank=True, null=True, max_length=100
    )
    groups = models.ManyToManyField(Group, related_name="custom_user_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions"
    )
