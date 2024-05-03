from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password


class Permission(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    permission = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError('Foydalanuvchi nomeri majburiy.')

        user = self.model(
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password=None):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=30, null=True, blank=True)
    lastname = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=30, unique=True, null=True)
    phone_number = models.CharField(max_length=13, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return "%s" % self.phone_number
