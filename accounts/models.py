from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from portals.choices import UserChoices
import uuid
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractBaseUser):
    id         = models.UUIDField(default=uuid.uuid4,primary_key=True)
    email      = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_admin         = models.BooleanField(default=False)
    username         = models.CharField(max_length = 50)
    profile_pic      = models.ImageField(upload_to="user/",null=True,blank=True)
    mobile_number    = models.CharField(max_length=20,unique=True,blank=True,null=True)
    city             = models.CharField(max_length = 50 ,blank=True, null=True)
    user_type        = models.CharField(choices=UserChoices.choices,default=UserChoices.ACCOUNTANT,max_length=250)
    country          = models.CharField(max_length=50,default="India")
    accepted_policy  = models.BooleanField(default=False)

    created_on       = models.DateTimeField(auto_now_add=True,editable=False)
    updated_on       = models.DateTimeField(auto_now=True)
    is_active        = models.BooleanField(default=True)

    
    objects    = UserManager()
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def __str__(self) -> str:
        return self.email
    

    def save(self, *args, **kwargs):
        # Check if user_role is not set and assign the default role
        if not self.user_role_id:
            default_role = UserRole.objects.get(role_name='Normal')  
            self.user_role = default_role
        # Call the original save method
        super().save(*args, **kwargs)
