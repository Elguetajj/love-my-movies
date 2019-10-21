FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential redis-server
COPY myapp /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["bash","./start.sh"]
