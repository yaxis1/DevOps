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

Once the services are up, we need to integrate this in a Jenkins CI CD pipeline. 
