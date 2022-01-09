from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import User

# Create your views here.

def index(request):

    return render(request, 'register.html')
