This Branch is an alternative approach to linux_branch

Here we try to integarte nginx to application, using another docker.

![image](https://user-images.githubusercontent.com/38083799/139084207-3aa4391a-d3b0-4d7d-9c44-c3d42331abb2.png)

This branch contains the same application from linux_branch but this time we use 'ubuntu' image in docker file instead of python image. This is required as we are going to install uwsgi on the instance.


# app
The app folder contains flask application running on localhost:2021

The Dockerfile calls an ubuntu image instead of python image, installs required packages, copies all files from host to docker directory and runs the application on uwsgi.

# nginx

This folder contains A docker file and nginx configuration file.

The Docker calls nginx image from docker hub and replaces the default nginx.conf file with our own file.

The modified nginx.conf listens to traffic on port 80 and redirects to our application that is running on 2021.

### Running Dockercompose

This branch calls an ubuntu image instead of python image, installs required packages, copies all files from host to docker directory and runs the application on uwsgi. 

Also introduces a nginx server, this time the second docker (with nginx image) depends on ubuntu server that installs nginx.

Once application is running, the second docker is built to listen on port 2021

```
docker-compose build
docker-compose up
```
![image](https://user-images.githubusercontent.com/38083799/139088226-eedb464b-f17a-42a3-84fa-88805115bd76.png)

![image](https://user-images.githubusercontent.com/38083799/138889931-3363b381-de58-4e58-a5a2-73de90d4c8db.png)

![image](https://user-images.githubusercontent.com/38083799/139087087-f99b807b-37c3-4e7b-9374-d0dc79993e7f.png)

As the screenshots show, first the application docker is built then nginx starts to fetch its configuration from default location /etc/nginx/conf.d/default.conf , however the second docker is built that replaces this file with custom configuration file that tells nginx to start looking on port 2021.

This can be integrated with Jenkins adding additional pipeline just like branch 'linux_branch'


