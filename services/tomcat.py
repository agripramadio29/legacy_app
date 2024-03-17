import subprocess
import os

def stop():
    message = ""
    try:
        subprocess.run(["bash","/usr/local/tomcat/bin/shutdown.sh"], check=True)
        message = "Apache Tomcat turned off successfully"
    except subprocess.CalledProcessError as e:
        message = f"Error while shutting down Apache Tomcat, {e}"
    except FileNotFoundError as f:
        message = f"{os.name} is not compatible with Legacy :("
    return message

def start():
    message = ""
    try:
        result = subprocess.run(["bash", "/usr/local/tomcat/bin/startup.sh"], check=True)
        message = "Apache Tomcat successfully started"
    except subprocess.CalledProcessError as e:
        message = f"Error while starting Apache Tomcat, {e}"
    except FileNotFoundError as f:
        message = f"{os.name} is not compatible with Legacy :("
    return message

def restart():
    message = ""
    try:
        subprocess.run(["bash","/usr/local/tomcat/bin/shutdown.sh"], check=True)
        subprocess.run(["bash","/usr/local/tomcat/bin/startup.sh"], check=True)
        message = "Apache Tomcat restarted successfully"
    except subprocess.CalledProcessError as e:
        message = f"Error while restarting Apache Tomcat, {e}"
    except FileNotFoundError as f:
        message = f"{os.name} is not compatible with Legacy :("
    return message