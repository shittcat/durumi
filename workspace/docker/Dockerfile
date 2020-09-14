#docker build --no-cache --network=host -t durumi .
#docker run -it --net host --name durumi durumi /bin/bash

FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3.6=3.6.9-1~18.04ubuntu1.1 
RUN apt-get install -y python3-pip
RUN apt-get install -y net-tools
RUN apt-get install -y dnsutils
RUN apt-get install -y wget
WORKDIR /home
RUN pip3 install pip==20.2.1
RUN pip3 install django==3.0.4
RUN pip3 install gunicorn==20.0.2
RUN pip3 install bcrypt
RUN pip3 install simplejson

RUN apt-get install -y libmysqlclient-dev=5.7.31-0ubuntu0.18.04.1
RUN pip3 install mysqlclient

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENTRYPOINT ["dockerize", "-wait", "tcp://mysql_service:3306", "-timeout", "20s"]