This project follows a simple REST application integrating it with continuous integration and continuous continuous deployment on a Docker container while trying to implement a microservice.  

The REST app has 5 input and 1 output parameters that is included with a html file.

The app runs on port 2021 - The app and all it's contents will be pushed to a linux instance to take better advantage of dockers.

#Docker Installation: 
```
sudo apt-get update
sudo apt-get upgrade
sudo apt install docker.io
systemctl start docker
systemctl enable docker
docker --version
```


