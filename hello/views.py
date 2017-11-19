from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import os
from .models import Greeting, Budget

# Create your views here.
def index(request):
    return render(request, 'index.html')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

def getData(request):
    bud = Budget.objects.all()
    return HttpResponse(bud)
