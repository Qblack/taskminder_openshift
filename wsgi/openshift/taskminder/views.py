from django.shortcuts import render
from taskminder.models import Assignment

# Create your views here.

def show_assignments(request):
    assignments = Assignment.objects.all()
    context = {'assignments':assignments}

    return  render(request,'home/assignments.html',context)