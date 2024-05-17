from django.db import models
from django.contrib.auth.models import AbstractUser , Group , Permission
from django.core.validators import MinValueValidator,RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.

class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True,null=True,unique=True)
    password = models.CharField(max_length=15)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18)])
    phone = models.CharField(max_length=13,validators=[RegexValidator(
         regex= r'^\+98\d{10}$',
         message='Phone number must be entered in the format: +98xxxxxxxxxx'
    )])

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def save(self,*args,**kwargs):
         
         self.username = f'{self.first_name} {self.last_name}'
         super().save(*args,**kwargs)
         


    def clean(self) -> None:
         
         super().clean()
         if self.age <18:
              raise ValidationError("Age must be at least 18")
         

    class Meta:
         
         verbose_name = 'User'
         verbose_name_plural = 'Users'
         ordering = ['last_name','first_name']

    
    def __str__(self) -> str:
         return self.username


