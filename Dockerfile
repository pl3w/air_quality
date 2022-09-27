FROM continuumio/miniconda3

RUN apt-get update

RUN mkdir /air_quality

COPY . /air_quality
WORKDIR /air_quality

RUN pip install pipenv 
RUN pipenv sync

RUN VERSION=RELESE python genenv.py
