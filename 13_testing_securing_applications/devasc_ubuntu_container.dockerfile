# Ubuntu based image
FROM ubuntu:lastest
COPY install.sh /app
VOLUME /app
RUN apt-get update && \
    apt-get install -qy \
    python3.9
RUN ["/bin/sh", "-c", "/app/install.sh"]
EXPOSE 8080