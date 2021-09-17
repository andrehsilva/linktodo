from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Links

# Create your views here.

def home_links(request):
    links = Links.objects.all()
    return render(request, 'index.html', {'links': links})

