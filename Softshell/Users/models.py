from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager, PermissionsMixin):
    def create_user(self, user_id, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('Vous devez entrer un email')
        
        user_obj = self.model(
                    email = self.normalize_email(email),
                    user_id = self.user_id,
                    first_name = self.first_name,
                    last_name = self.last_name
                    )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    # def create_superuser(self, user_id, first_name, last_name, email, password=None):





class Users(AbstractBaseUser):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=128, blank=False)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Contributors(models.Model):
    user_id = models.IntegerField(primary_key=True) # Foreign key ?
    project_id = models.IntegerField(blank=False)
    permission = models.IntegerField(blank=False) # Choices ?
    role = models.CharField(max_length=128)