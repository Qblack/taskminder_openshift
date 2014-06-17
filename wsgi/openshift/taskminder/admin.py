from taskminder.forms import userforms
from django.contrib import admin
from taskminder.models import Task, Course, Professor, University, Country, Province, UserProfile
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Register your models here.

admin.site.register(Task)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(University)
admin.site.register(Province)
admin.site.register(Country)


# Now register the new UserAdmin...
admin.site.register(UserProfile, userforms.MyUserAdmin)



