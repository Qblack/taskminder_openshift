from django.shortcuts import render
from taskminder.models import Task
from taskminder.forms.userforms import LogInForm, UserCreationForm
from taskminder.forms.courseform import AddCourseForm, JoinCourseForm, SelectUniversityForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, get_user_model

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        login_form = LogInForm(request.POST)
        if login_form.is_valid():
            user = login_form.login(request)
            if user:
                login(request,user)
                request.session['user_id'] = user.id
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


def course_add_view(request):

    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = AddCourseForm()
    return render(request,'Course/add_course.html',{'form':form,})


@login_required
def course_join_view(request):

    if request.method == 'POST':
        form = JoinCourseForm(request.POST)
        if form.is_valid():
            for course in form.cleaned_data.get('courses'):
                user_id = request.session['user_id']
                user = get_user_model().objects.get(id=user_id)
                user.courses.add(course)

            return HttpResponseRedirect('/thanks/')
    else:
        form = JoinCourseForm()
    return render(request,'Course/join_course.html',{'form':form,})

@login_required
def show_assignments(request):
    assignments = Task.objects.get(type='Assignment').all()
    context = {'assignments':assignments}

    return  render(request,'home/assignments.html',context)

@login_required
def show_my_tasks_view(request):
    print("Hello World")
    user = get_user_model().objects.get(id=request.session['user_id'])

    tasks=[]
    for course in user.courses.all():
        course_tasks = Task.objects.filter(course=course.id)
        for task in course_tasks:
            tasks.append(task)

    context = {'tasks':tasks}

    return  render(request,'Tasks/show_tasks.html',context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/thanks/')



