from django.shortcuts import render
import subprocess
from django.http import HttpResponse
import os
from services import tomcat, postgresql
from django.shortcuts import redirect
from django.urls import reverse
from legacy_app import apputils
import sweetify

# Create your views here.
def home_view(request):
    status = request.GET.get('status', None)
    return render(request, "index.html", {'status': status})

def about(request):
    return render(request, "about.html")

def legacy(request):
    return redirect('home')

# PREDEFINED SERVICES

def pg_stop(request):
    code = postgresql.stop()
    sweetify.success(request, apputils.process_results("PostgreSQL", "stopp", code)) if code == 1 else sweetify.error(request, apputils.process_results("PostgreSQL", "stopp", code))
    return redirect('/')


def pg_start(request):
    code = postgresql.start()
    sweetify.success(request, apputils.process_results("PostgreSQL", "start", code)) if code == 1 else sweetify.error(request, apputils.process_results("PostgreSQL", "start", code))
    return redirect('/')
    
def pg_restart(request):
    code = postgresql.restart()
    sweetify.success(request, apputils.process_results("PostgreSQL", "restart", code)) if code == 1 else sweetify.error(request, apputils.process_results("PostgreSQL", "restart", code))
    return redirect('/')

#TOMCAT SERVICE

def at_status(request):
    status = tomcat.check_status()
    return redirect(reverse('home') + '?status=' + status)

def at_stop(request):
    code = tomcat.stop()
    sweetify.success(request, apputils.process_results("Apache Tomcat", "stopp", code)) if code == 1 else sweetify.error(request, apputils.process_results("Apache Tomcat", "stopp", code))
    return redirect('/')

def at_start(request):
    code = tomcat.start()
    sweetify.success(request, apputils.process_results("Apache Tomcat", "start", code)) if code == 1 else sweetify.error(request, apputils.process_results("Apache Tomcat", "start", code))
    return redirect('/')


def at_restart(request):
    code = tomcat.restart()
    sweetify.success(request, apputils.process_results("Apache Tomcat", "restart", code)) if code == 1 else sweetify.error(request, apputils.process_results("Apache Tomcat", "restart", code))
    return redirect('/')

def download_logs(request):
    code = tomcat.download_logs()
    sweetify.success(request, "ok") if code == 1 else sweetify.error(request, "fail")
    return redirect("/")


# ENDBLOCK




