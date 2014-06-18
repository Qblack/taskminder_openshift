from django.shortcuts import render
from taskminder.models import Task
from taskminder.forms.userforms import LogInForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        login_form = LogInForm(request.POST)
        if login_form.is_valid():
            user = login_form.login(request)
            if user:
                login(request,user)
                return HttpResponseRedirect("/thanks/")
    else:
        login_form = LogInForm()
    return render(request,'User/login.html',{'form':login_form,})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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

