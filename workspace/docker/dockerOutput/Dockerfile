FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3.6=3.6.9-1~18.04ubuntu1
RUN apt-get install -y python3-pip=9.0.1-2.3~ubuntu1.18.04.1
RUN apt-get install -y net-tools
RUN apt-get install -y dnsutils
RUN apt-get install -y vim

WORKDIR /home
RUN pip3 install pip==20.0.2
RUN pip install django==3.0.4
RUN pip install gunicorn==20.0.2
