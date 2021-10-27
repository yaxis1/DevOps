This project follows a simple REST application integrating it with continuous integration and continuous continuous deployment on a Docker container while trying to implement a microservice.  

![image](https://user-images.githubusercontent.com/38083799/139068751-77d3a1c1-d20e-45b4-b492-aac596270741.png)

# app
The app folder contains flask application running with waitress since flask default is not suitable for production environment.

The Dockerfile calls a python image, copies all files from host to docker directory and runs the application.

Requirements.txt is generating from pip freeze to capture all libraries of current environment.

Then, there are templates for the flask app which takes inputs from html form.

test.py imports the testing module 'unittest' that does few tests to check if the status code is accurate and output is as expected.

The REST app has 5 input and 1 output parameters that is included with a html file.

The app runs on port 2021 - The app and all it's contents will be pushed to a linux instance(Windows Subsytem for Linux) to take better advantage of dockers.

# Docker Installation: 
```
sudo apt-get update
sudo apt-get upgrade
sudo apt install docker.io
systemctl start docker
systemctl enable docker
docker --version
```

A Dockerfile is created that uses python3 image and installs are requirements from requirements.txt, the choice of a python docker image has been made instead of linux image to speed up deployment.

### Building docker image:

The Dockerfile calls a python image, copies all files from host to docker directory and runs the application.

```
docker build -t app
docker run app
```

This builds the docker from Dockerfile inside app folder. 

### Running Dockercompose

Docker compose makes it easier to integrate with multiple dockers, instead of writing a seperate docker file for each service, we can draft a docker-compose.yml, opening particular ports and attaching required volumes for respective services.

To illustrate DockerCompose, we introduce a service that depends on main application, docker compose defines ports and dependability features on multiple dockers.

```
docker-compose build
docker-compose up
```

![image](https://user-images.githubusercontent.com/38083799/138735378-44fa2c46-cdcd-4eda-b0a3-3e2154f117de.png)
![image](https://user-images.githubusercontent.com/38083799/138735423-ef73f470-004a-4abe-90ee-98a2dc060b77.png)

Once the services are up, we need to integrate this in a Jenkins CI CD pipeline. 


# Jenkins Installation
Jenkins can be installed either on the linux instance or local machine, since it is a production environment, it is a best practise to have jenkins portal available on local machine.

A Java runtime is required for jenkins to run, after installing java, we move to jenkins directory and start jenkins.

```
java -jar jenkins.war
```

Once it is started, we will have an admin password which should be inserted on jenkins portal that is running on localhost:8080.

We will use pipeline feature of jenkins
1. Check if the REST API is working as expected 
2. Check if tests are successful 
2. Check if Dockers are successfully deployed and hosting the application.



This jenkins is configured to pull from github repository (linux_branch) 

### Jenkins File

We can define a pipeline inside Jenkinsfile that has multiple stages, each stage is individually monitored on Jenkins Portal. To make this more easier, we write a .groovy script that has individual functions returning respective commands - this script can be called as a main function inside Jenkins file. 

In the JenkinsFile:
#### Stage 1 

loads groovy script into a variable that can be further called and installing requirements from requirements.txt that is defined as installRequirements() inside .groovy script.

#### Stage 2

Builds application by calling function runApp() that returns command 'python3 ./app/run.py'

#### Stage 3

Tests application by calling runTest() from .groovy script

#### Stage 4 

Deploys dockers 


![image](https://user-images.githubusercontent.com/38083799/138784350-9af8e651-e575-4253-a182-8920ded42eef.png)

![image](https://user-images.githubusercontent.com/38083799/138781004-a627f4ba-f1f7-4af7-a19b-380ef6a02c3c.png)

In the image above, we can see the pipeline terminated due to failure after 3rd stage, as soon as this is fixed and the repository is pushed, jenkins will run the pipeline again and try to Deploy the application.

After, fixes and lot of git commits, the final pipeline looks like this which successful builds and Application Deployment: 

![image](https://user-images.githubusercontent.com/38083799/139080421-4b3aaf31-07fc-453f-a5f1-c99abfe1080b.png)

