import subprocess
import os
import requests

def check_status():
    status = ""
    try:
        req = requests.get('http://10.12.4.164:8777')
        status = "Active"
    except ConnectionRefusedError as x:
        status = "Inactive"
    except Exception as f:
        status = "Inactive"
    return status

def stop():
    code = 0
    try:
        subprocess.run(["bash","/usr/local/tomcat2/bin/shutdown.sh"], check=True)
        code = 1
    except subprocess.CalledProcessError as e:
        code = -1
    except FileNotFoundError as f:
        code = -2
    return code

def start():
    code = 0
    try:
        subprocess.run(["bash","/usr/local/tomcat2/bin/startup.sh"], check=True)
        code = 1
    except subprocess.CalledProcessError as e:
        code = -1
    except FileNotFoundError as f:
        code = -2
    return code

def restart():
    code = 0
    try:
        subprocess.run(["bash","/usr/local/tomcat2/bin/shutdown.sh"], check=True)
        subprocess.run(["bash","/usr/local/tomcat2/bin/startup.sh"], check=True)
        code = 1
    except subprocess.CalledProcessError as e:
        code = -1
    except FileNotFoundError as f:
        code = -2
    return code
