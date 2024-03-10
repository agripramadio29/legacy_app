from django.shortcuts import render
import subprocess
from django.http import HttpResponse
import os
# Create your views here.
def home_view(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def pg_stop(request):
    message = ""
    try:
        subprocess.run(["systemctl", "stop", "postgresql"], check=True)
        message = "PostgreSQL service has been stopped."
        return render(request, "success.html", {'message' : message})
    except subprocess.CalledProcessError as e:
        message = f"Error while stopping PostgreSQL, {e}"
        return render(request, "failed.html", {'message' : message})
    except FileNotFoundError as f:
        message = f"{os.name} is not compatible with this Web App"
        return render(request, "failed.html", {'message' : message})

def pg_start(request):
    message = ""
    try:
        subprocess.run(["systemctl", "start", "postgresql"], check=True)
        message = "PostgreSQL service has been started."
        return render(request, "success.html", {'message' : message})
    except subprocess.CalledProcessError as e:
        message = f"Error while starting PostgreSQL, {e}"
        return render(request, "failed.html", {'message' : message})
    except FileNotFoundError as f:
        message = f"{os.name} is not compatible with this Web App"
        return render(request, "failed.html", {'message' : message})
    
def pg_restart(request):
        message = ""
        try:
            subprocess.run(["systemctl", "restart", "postgresql"], check=True)
            message = "PostgreSQL service has been restarted."
            return render(request, "success.html", {'message' : message})
        except subprocess.CalledProcessError as e:
            message = f"Error while restarting PostgreSQL, {e}"
            return render(request, "failed.html", {'message' : message})
        except FileNotFoundError as f:
            message = f"{os.name} is not compatible with this Web App"
            return render(request, "failed.html", {'message' : message})