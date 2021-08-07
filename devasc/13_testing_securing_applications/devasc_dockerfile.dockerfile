# specifies the base image to be used for the Dockerfile
FROM ubuntu:latest

# argument passed into the docker run command - can be placed before FROM if needed for the FROM instruction
ARG install_file

# copies the argument passed to the app dir
COPY $install_file/app

# creates a new environment variable or sets a value to an existing variable inside the container
# using '=' enables you to set multiple variables in the same instruction
ENV app_name="Install File", app_maintainer=John\ Smith, app_directory=/opt/app

# used to run single or multiple commands in the shell to prepare the image
# the shell form runs the command in the shell with bin/sh -c:
RUN apt-get update && \
    apt-get install -qy \
    python3.9 \

# running commands in the exec form requires a definition of the shell to be used and the commands split up
RUN ["/bin/bash", "-c", "echo $HOME"]
RUN make/app

# creates a mounting point for persisting data that is consumed by the Docker container
# volumes are managed by Docker and do not get deleted when the container stops running
VOLUME /opt/app

# exposes a TCP or UDP port on which the application running in the container is accessible
EXPOSE 80

# CMD does not execute when the image is building, it executes when the new container is started
# this would start a webserver once the image is running
CMD /usr/sbin/httpd