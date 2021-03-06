from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_active=True, is_admin= False, is_staff=False):
        if not email:
            raise ValueError("Users must have email")
        if not password:
            raise ValueError('users must have a password')
        user_obj = self.model(
            email = self.normalize_email(email)
            )
        user_obj.username = username
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self,  email, username, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
            is_admin=True,
            is_staff=True
        )
        return user

class User(AbstractBaseUser):
    username = models.CharField(default= 'Yamama',max_length=50,unique=True)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default= True)
    confirm = models.BooleanField(default= True)
    created_date=models.DateTimeField(auto_now_add=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    objects= UserManager()
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Username']

    def __str__(self):
        return self.email
    def get_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_staff(self):
        return self.staff

# Create your models here.
