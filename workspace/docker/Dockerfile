#docker build --no-cache --network=host -t durumi .
#docker run -it --net host --name durumi durumi /bin/bash

FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3.6
RUN apt-get install -y python3-pip
RUN apt-get install -y net-tools
RUN apt-get install -y dnsutils
RUN apt-get install -y wget
WORKDIR /home
RUN pip3 install pip
RUN pip3 install django
RUN pip3 install gunicorn
RUN pip3 install bcrypt
RUN pip3 install simplejson
RUN pip3 install haversine 

RUN apt-get install -y libmysqlclient-dev
RUN pip3 install mysqlclient

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENTRYPOINT ["dockerize", "-wait", "tcp://mysql_service:3306", "-timeout", "60s"]
