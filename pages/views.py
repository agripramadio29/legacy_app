from django.shortcuts import render
import subprocess
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    return render(request, "index.html")

def execute_bash_script(request):
    try:
        subprocess.run(["systemctl", "stop", "postgresql"], check=True)
        return HttpResponse("PostgreSQL service has been stopped.")
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Error: {e}")

