from django.shortcuts import render
import subprocess
from django.http import HttpResponse
import os
from services import tomcat, postgresql
# Create your views here.
def home_view(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

# PREDEFINED SERVICES

def pg_stop(request):
    message = postgresql.stop()
    return render(request, "success.html", {'message': message})

def pg_start(request):
    message = postgresql.start()
    return render(request, "success.html", {'message': message})
    
def pg_restart(request):
    message = postgresql.restart()
    return render(request, "success.html", {'message': message})

#TOMCAT SERVICE

def at_stop(request):
    message = tomcat.stop()
    return render(request, "success.html", {"message": message})

def at_start(request):
    message = tomcat.start()
    return render(request, "success.html", {"message": message})


def at_restart(request):
    message = tomcat.restart()
    return render(request, "success.html", {"message": message})


# ENDBLOCK




