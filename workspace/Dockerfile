FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3.6=3.6.9-1~18.04ubuntu1
RUN apt-get install -y python3-pip=9.0.1-2.3~ubuntu1.18.04.1
RUN apt-get install -y net-tools
RUN apt-get install -y dnsutils
WORKDIR /home
RUN pip3 install pip==20.0.2
RUN pip3 install django==3.0.4
RUN pip3 install gunicorn==20.0.2

RUN apt-get install -y libmysqlclient-dev=5.7.31-0ubuntu0.18.04.1
RUN pip3 install mysqlclient