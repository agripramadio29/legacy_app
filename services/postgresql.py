import subprocess
import os

def stop():
    code = 0
    try:
        subprocess.run(["systemctl", "stop", "postgresql"], check=True)
        code = 1
    except subprocess.CalledProcessError as e:
        code = -1
    except FileNotFoundError as f:
        code = -2
    return code

def start():
    code = 0
    try:
        subprocess.run(["systemctl", "start", "postgresql"], check=True)
        code = 1
    except subprocess.CalledProcessError as e:
        code = -1
    except FileNotFoundError as f:
        code = -2
    return code

def restart():
    code = 0
    try:
        subprocess.run(["systemctl", "restart", "postgresql"], check=True)
        code = 1
    except subprocess.CalledProcessError as e:
        code = -1
    except FileNotFoundError as f:
        code = -2
    return code