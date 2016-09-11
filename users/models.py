from __future__ import unicode_literals
from random import randint

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models


def get_random():
  return randint(1, 100)


class UserManager(BaseUserManager):
    def create_user(self, email, birthday, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            birthday=birthday,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    birthday = models.DateField()
    rnd_number = models.IntegerField(default=get_random)
    first_name = models.CharField(blank=True, null=True, max_length=128)
    last_name = models.CharField(blank=True, null=True, max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birthday',]

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin