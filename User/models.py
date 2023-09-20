from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
#from shortuuid.django_fields import ShortUUIDField


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password, **extra_fields):
        """
          Create and save a SuperUser with the given email,first name , lastname and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('Username must be set'))
        if not password:
            raise ValueError(_('Password must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email,first name , lastname and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    bio = models.CharField(max_length=200, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='Avatars/')
    portfolio = models.URLField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    # required for creating user
    REQUIRED_FIELDS = ['email',]

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return f'{self.username}'