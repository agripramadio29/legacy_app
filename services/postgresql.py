import subprocess
import os

def stop():
    message = ""
    try:
        subprocess.run(["systemctl", "stop", "postgresql"], check=True)
        message = "PostgreSQL service has been stopped."
    except subprocess.CalledProcessError as e:
        message = f"Error while stopping postgresql, {e}"
    except FileNotFoundError as f:
        message = f"{os.name} is not compatible with Legacy :("
    return message

def start():
    message = ""
    try:
        subprocess.run(["systemctl", "start", "postgresql"], check=True)
        message = "PostgreSQL service has been started."
    except subprocess.CalledProcessError as e:
        message = f"Error while starting postgresql, {e}"
    except FileNotFoundError as f:
        message = f"{os.name} is not compatible with Legacy :("
    return message

def restart():
    message = ""
    try:
        subprocess.run(["systemctl", "restart", "postgresql"], check=True)
        message = "PostgreSQL service has been restarted."
    except subprocess.CalledProcessError as e:
        message = f"Error while restarting postgresql, {e}"
    except FileNotFoundError as f:
        message = f"{os.name} is not compatible with Legacy :("
    return message