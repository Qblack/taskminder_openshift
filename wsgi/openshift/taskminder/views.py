from django.shortcuts import render
from taskminder.models import Task
from taskminder.forms.loginform import LogInForm
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = LogInForm()
    return render(request,'User/login.html',{'form':form,})


def show_assignments(request):
    assignments = Task.objects.get(type='Assignment').all()
    context = {'assignments':assignments}

    return  render(request,'home/assignments.html',context)

