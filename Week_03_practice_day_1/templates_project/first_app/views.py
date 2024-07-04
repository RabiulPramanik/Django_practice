from django.shortcuts import render
from django.http import HttpResponse
from django import template
import datetime

def home(request):
    context = {
        'name':"robiul islam",
        'id':2108015,
        'age':24,
        'brithday':datetime.datetime.now(),
        'list':['I','am','a','Mechatronics','Engineer'],
        'complete_course':[
            {
                'id':1,
                'name':'Basic c and c++'
            },
            {
                'id':2,
                'name':'Basic DSA'
            },
            {
                'id':3,
                'name':'Basic JAVA'
            },
            {
                'id':1,
                'name':'Database'
            },
            {
                'id':1,
                'name':'Software engineering'
            },
        ],
    }
    return render(request, "first_app/home.html",context)
