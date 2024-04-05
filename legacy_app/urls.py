"""legacy_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),

    #services
    path('pg_stop', views.pg_stop, name='pg_stop'),
    path('pg_start/', views.pg_start, name='pg_start'),
    path('pg_restart/', views.pg_restart, name='pg_restart'),
    path('at_start/', views.at_start, name='at_start'),
    path('at_stop/', views.at_stop, name='at_stop'),
    path('at_restart/', views.at_restart, name='at_restart'),
    path('at_status/', views.at_status, name='at_status'),
    path('legacy/', views.legacy, name='legacy'),
    path('download_logs/', views.download_logs, name='download_logs'),

    path('about/', views.about, name="about")

]
