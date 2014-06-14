from django.contrib import admin
from tasks.models import Assignment, Reading, Test


# Register your models here.


admin.site.register(Assignment)
admin.site.register(Reading)
admin.site.register(Test)