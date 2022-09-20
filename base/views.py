from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse

rooms = [
            {'id': 1, 'name':'Django Tuts'},
            {'id': 2, 'name':'NodeJS tuts'},
            {'id': 3, 'name':'Springboot Tuts'}
        ]

def home(request):
    return render(request, 'home.html')

def room(request):
    context = {'rooms': rooms}
    return render(request, 'room.html', context)