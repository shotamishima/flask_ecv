FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /flask_project
WORKDIR /opt
RUN wget http://repo.continuum.io/archive/Anaconda3-2020.02-Linux-x86_64.sh && \
	sh Anaconda3-2020.02-Linux-x86_64.sh -b -p /opt/anaconda3  && \
ENV PATH /opt/anaconda3/bin:$PATH
WORKDIR /flask_project
