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
    contexts = {}
    try:
        result = subprocess.run(["bash", "/usr/local/tomcat/bin/startup.sh"], capture_output=True, text=True, check=True)
        output = result.stdout
        message = "Apache Tomcat successfully started"
        contexts.update({"output": output})
        contexts.update({"message": message})
    except subprocess.CalledProcessError as e:
        message = f"Error while starting Apache Tomcat, {e}"
        contexts.update({"message": message})
    except FileNotFoundError as f:
        message = f"{os.name} is not compatible with Legacy :("
        contexts.update({"message": message})
    return contexts

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