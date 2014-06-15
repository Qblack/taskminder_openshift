from django.shortcuts import render_to_response
from taskminder.fill_data import transfer_database

def home(request):
     return render_to_response('home/home.html')

def load(request):
    transfer_database()
    return  render_to_response('home/load_database.html')