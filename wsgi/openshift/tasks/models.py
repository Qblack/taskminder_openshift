from django.db import models

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    course = models.OneToOneField(Course)

    def __unicode__(self):
        return self.title

class Reading(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    course = models.OneToOneField(Course)
    pages = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title

class Test(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    course = models.OneToOneField(Course)

    def __unicode__(self):
        return self.title


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    course_section = models.CharField(max_length=10)
    professor = models.OneToOneField(Professor)

    def __unicode__(self):
        return self.course_name+' '+self.course_section

class Professor(models.Model):
    name = models.CharField(max_length=200)
    universities = models.ManyToManyField(University)

    def __unicode__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=200)
    province = models.OneToOneField(Province)

    def __unicode__(self):
        return self.name

class Country(models.Model):
    SCHOOLS = ('Canada',)
    name = models.CharField(max_length=200,choices=SCHOOLS)
    def __unicode__(self):
        return self.name

class Province(models.Model):
    PROVINCE_CHOICES = ('Ontario',)
    name = models.CharField(max_length=20,choices=PROVINCE_CHOICES)
    country = models.OneToOneField(Country)

    def __unicode__(self):
        return self.name



