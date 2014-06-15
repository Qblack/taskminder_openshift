from django.contrib import admin
from taskminder.models import Assignment, Reading, Test, Course, Professor, University, Country, Province

# Register your models here.

admin.site.register(Assignment)
admin.site.register(Reading)
admin.site.register(Test)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(University)
admin.site.register(Province)
admin.site.register(Country)

