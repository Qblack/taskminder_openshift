from django.shortcuts import render
from taskminder.models import Task
from taskminder.forms.userforms import LogInForm, UserCreationForm
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = UserCreationForm()
    return render(request,'User/register_new_user.html',{'form':form,})

def thanks(request):
    return render(request,'home/thanks.html')

def show_assignments(request):
    assignments = Task.objects.get(type='Assignment').all()
    context = {'assignments':assignments}

    return  render(request,'home/assignments.html',context)

