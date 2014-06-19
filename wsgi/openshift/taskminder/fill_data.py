from django.shortcuts import render

__author__ = 'Q'

import sqlite3
from taskminder.models import Task, Course
from django.utils.dateparse import parse_date, parse_time

TYPES = ['Reading', 'Assignment', 'Test','Course']
def transfer_database():
    db = sqlite3.connect("C:/Users/Q/Envs/Python33/SchedualeMaker/summer2014courses.db")

    copy_deliverable(db,TYPES[1],Task)
    copy_deliverable(db,TYPES[2],Task)
    copy_reading(db)
    db.close()
    return


def copy_deliverable(db,deliverable_type, class_type):
    entries = select_homework(deliverable_type,db)
    for deliverable in entries:
        course = Course.objects.get(course_code=deliverable[0])
        date = parse_date(deliverable[2])
        if deliverable[3] is not None:
            time = parse_time(deliverable[3])
        else:
            time=None
        new_task = class_type(title=deliverable[1],
                                    due_date=date,
                                    time=time,
                                    course=course,
                                    type=deliverable_type
                                    )
        new_task.save()

    return

def copy_reading(db):
    entries = select_homework('Reading',db)
    for reading in entries:
        course = Course.objects.get(course_code=reading[0])
        date = parse_date(reading[3])
        new_reading = Task(title=reading[1],
                                    due_date=date,
                                    pages = reading[4],
                                    course=course,
                                    type='Reading',
                                    )
        new_reading.save()
    return


def copy_courses(db):
    entries = select_homework('Courses',db)
    print(entries)
    for course in entries:
        new_course = Course(course_code=course[0],
                            course_name=course[1]
                            )
        new_course.save()

    return

def select_homework(homework_type,db):
    sql = '''SELECT * FROM {0}s;'''.format(homework_type)
    cur = db.execute(sql)
    entries = cur.fetchall()
    return entries

def load_data_view(request):
    transfer_database()
    return render(request,'home/load_database.html',)
