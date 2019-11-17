FROM python:3.7

MAINTAINER Ozan Teoman DAYANAN <ozanteomandayanan@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN mkdir /django_backend

WORKDIR /django_backend

ADD requirements.txt /django_backend/

RUN pip3 install --upgrade pip
RUN pip3 install ipython
RUN pip3 install -r requirements.txt

ADD . /django_backend/


