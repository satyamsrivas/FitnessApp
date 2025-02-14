from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from core.models import BaseModel
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,mobile_number,first_name=None,password=None):
        if not mobile_number:
            raise ValueError("User Must have a mobile number")
        user = self.model(
            mobile_number = mobile_number,
            first_name = first_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,mobile_number,first_name=None,password=None):
        user = self.create_user(
            mobile_number=mobile_number,
            first_name = first_name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(BaseModel,AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20,null=True,blank=True)
    mobile_number = models.CharField(max_length=12,unique=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    

    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = ["first_name"]

    objects = UserManager()

    def __str__(self):
        return "{} {}-{}".format(self.first_name,self.last_name,self.mobile_number)

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True


class FitnessProfile(BaseModel):
    class GenderChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', "Female"
        OTHER = 'O', "Other"
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='fitness_profile',null=True)
    height = models.DecimalField(max_digits=6,decimal_places=2,help_text="Enter Your Height In Cm")
    weight = models.DecimalField(max_digits=4,decimal_places=2,help_text="Enter Your Weight In Kg")
    age = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    gender = models.CharField(max_length=10,choices=GenderChoices.choices)
    
    @property
    def bmi(self):
        if self.height and self.weight:
            height_in_m = self.height / 100  # Convert cm to meters
            return round(self.weight / (height_in_m ** 2), 2)
        return None 
