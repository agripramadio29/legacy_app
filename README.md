# Project: Legacy

Legacy stands as a software tailored for seamless server management. 

As a DevOps Engineer, I frequently found myself immersed in the repetitive task of configuring servers, 
especially when it came to addressing specific errors that necessitated restarting PostgreSQL servers and Apache Tomcat webservers. 
Despite having Ansible at my disposal, the monotony persisted, especially for my Windows-using colleagues who had to resort to 
installing third-party SSH clients for their tasks. This additional step only added to the inertia, making the entire process cumbersome and time-consuming. 
It was during one particularly frustrating commute, trapped in the notorious Cawang Traffic Jam, that the idea for this application dawned on me. 
Frustrated by the manual slog of restarting services via SSH, I recognized the urgent need for a more efficient solution. 

Thus, this project was born - an application meticulously crafted to streamline the service restarting process, thereby eradicating the need for tedious manual interventions. 
Its purpose? To simplify the lives of both my colleagues and myself, ushering in a new era of productivity and efficiency in our server management endeavors.

This is the source code of Legacy. Feel free to use, download, modify, or even enhance this application. It's free and of course, open source!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need to install the software and how to install them:

- Linux Server / Workstation (Desktop) with root access. Currently, Legacy only supports Linux and UNIX type-OS
- Python 3 (I recommend Python 3.11) and pip
- Nginx (Optional)

### Installing

A step-by-step series of examples that tell you how to get the environment running.

1. Clone/Download the repository.

2. Navigate to the project directory.

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

### Usage

If you want to run the application in development mode:

    ```
    python3 manage.py runserver
    ```
Open your web browser and go to [http://localhost:8000](http://localhost:8000) to view the application.

In the requirements.txt, I've included gunicorn, which is django's production WSGI server for production deployments.
If you wish to deploy to a production environment, these are the steps:

    ```
    bash run.sh
    ```
Open your web browser and go to [http://localhost:8000](http://localhost:8000) to view the application. You'll notice that there is no bootstrap or other static files.
This is because gunicorn don't serve static files, therefore you need Nginx to serve those. If you have Nginx installed, open nginx.conf or default.conf (usually located
in /etc/nginx/) then add a block of reverse proxy code for this application.

Finally restart nginx by typing this command:

    ```
    systemctl restart nginx
    ```

Then the legacy app is ready for production use.

