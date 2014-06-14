from django.db import models

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    course_code = models.CharField(max_length=10)

    def __unicode__(self):
        return self.title

class Reading(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    course_code = models.CharField(max_length=10)
    pages = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title

class Test(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    course_code = models.CharField(max_length=10)

    def __unicode__(self):
        return self.title

