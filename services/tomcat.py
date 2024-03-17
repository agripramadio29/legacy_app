import subprocess
import os

def stop():
    message = ""
    try:
        subprocess.run(["bash","/usr/local/tomcat/bin/shutdown.sh"], check=True)
        message = "Apache Tomcat successfully turned off"
    except subprocess.CalledProcessError as e:
        message = f"Error while shutting down Apache Tomcat, {e}"
    except FileNotFoundError as f:
        message = f"{os.name} is not compatible with Legacy :("
    return message