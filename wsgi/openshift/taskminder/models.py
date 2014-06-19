from django.db import models
import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class Country(models.Model):
    CANADA = 'CA'
    COUNTRIES = ((CANADA,'Canada'),)
    name = models.CharField(max_length=200,choices=COUNTRIES)
    def __str__(self):
        return self.name

class Province(models.Model):
    ONTARIO = 'ON'
    PROVINCE_CHOICES = ((ONTARIO,'Ontario'),)
    name = models.CharField(max_length=20,choices=PROVINCE_CHOICES)
    country = models.OneToOneField(Country)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=200)
    province = models.OneToOneField(Province)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=200)
    universities = models.ManyToManyField(University)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    course_section = models.CharField(max_length=10)
    professor = models.ManyToManyField(Professor)

    def __str__(self):
        return self.course_name+'-'+self.course_section


class TaskminderUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('User must have an username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=200,unique=True,)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    program = models.CharField(max_length=200)
    universities = models.ManyToManyField(University)
    courses = models.ManyToManyField(Course)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = TaskminderUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','email','date_of_birth']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.username

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




class Task(models.Model):
    ASSIGNMENT = 'ASSIGN'
    QUIZ = 'QUIZ'
    MIDTERM = 'MID'
    READING = 'READ'
    FINAL = 'FINAL'
    TYPES = ((ASSIGNMENT,'Assignment'),
             (QUIZ,'Quiz'),
             (MIDTERM,'Midterm'),
             (READING,'Reading'),
             (FINAL,'Final'),
    )

    title = models.CharField(max_length=200)
    due_date = models.DateField('due date')
    course = models.ForeignKey(Course)
    pages = models.CharField(max_length=20,null=True,blank=True)
    time = models.TimeField(default=None,blank=True,null=True)
    type = models.CharField(max_length=30,choices=TYPES)

    def __str__(self):
        return self.title

class Completion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    task = models.ForeignKey(Task)
    completed = models.BooleanField(default=False)

