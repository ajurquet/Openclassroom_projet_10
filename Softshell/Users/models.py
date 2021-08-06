from Projects.models import Projects
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import (
                                    AbstractBaseUser,
                                    BaseUserManager,
                                    )
from django.db.models.deletion import CASCADE, RESTRICT


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Vous devez entrer un email.')
        
        user_obj = self.model(
                        email = self.normalize_email(email),
                        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email,
                                password=password,
                                )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email


class Contributors(models.Model):
    user_id = models.ForeignKey(Users, on_delete=CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=CASCADE)
    permission = models.  IntegerField(blank=False) # Choices ?
    role = models.CharField(max_length=128)