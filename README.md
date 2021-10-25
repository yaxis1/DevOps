This project follows a simple REST application integrating it with continuous integration and continuous continuous deployment on a Docker container while trying to implement a microservice.  

The REST app has 5 input and 1 output parameters that is included with a html file.

The app runs on port 2021 - The app and all it's contents will be pushed to a linux instance to take better advantage of dockers.

# Docker Installation: 
```
sudo apt-get update
sudo apt-get upgrade
sudo apt install docker.io
systemctl start docker
systemctl enable docker
docker --version
```

A Dockerfile is created that uses python3 image and installs are requirements from requirements.txt, the choice of a python docker image has been made instead of linux image to
speed up deployment.

### Building docker image:
```
docker build -t image-name
docker run <image id>
```

This builds the docker from Dockerfile, however, if we need to integrate more services in the app, we can use docker-compose.
Docker compose makes it easier to integrate with other docker instances, instead of writing a seperate docker file for each service, we can draft a docker-compose.yml, opening
particular ports and attaching required volumes for respective services.

### Running Dockercompose
```
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

We will use two features of Jenkins:
1. FreeStyle Project - to check if the REST API is working as expected and 
2. Pipeline to check - if Dockers are successfully deployed and hosting the website.
