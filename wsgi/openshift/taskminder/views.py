from django.shortcuts import render
from taskminder.models import Task

# Create your views here.

def show_assignments(request):
    assignments = Task.objects.get(type='Assignment').all()
    context = {'assignments':assignments}

    return  render(request,'home/assignments.html',context)