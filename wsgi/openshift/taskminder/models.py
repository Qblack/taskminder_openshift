from django.db import models

# Create your models here.
class Country(models.Model):
    CANADA = 'CA'
    COUNTRIES = ((CANADA,'Canada'),)
    name = models.CharField(max_length=200,choices=COUNTRIES)
    def __unicode__(self):
        return self.name

class Province(models.Model):
    ONTARIO = 'ON'
    PROVINCE_CHOICES = ((ONTARIO,'Ontario'),)
    name = models.CharField(max_length=20,choices=PROVINCE_CHOICES)
    country = models.OneToOneField(Country)

    def __unicode__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=200)
    province = models.OneToOneField(Province)

    def __unicode__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=200)
    universities = models.ManyToManyField(University)

    def __unicode__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    course_section = models.CharField(max_length=10)
    professor = models.OneToOneField(Professor)

    def __unicode__(self):
        return self.course_name+' '+self.course_section

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    course = models.OneToOneField(Course)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.title

class Reading(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    course = models.OneToOneField(Course)
    pages = models.CharField(max_length=20)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.title

class Test(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    course = models.OneToOneField(Course)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.title








