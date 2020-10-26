FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ENV SETUPTOOLS_USE_DISTUTILS stdlib

RUN mkdir /docker_api
WORKDIR /docker_api

USER root

COPY requirements.txt /docker_api
RUN pip3 install -r requirements.txt
# RUN pip install  -i  https://pypi.python.org/simple/  -r requirements.txt

COPY . /docker_api

RUN usermod -d /docker_api www-data \
&&  chown -R www-data:www-data /docker_api

USER www-data

RUN python3 manage.py collectstatic --clear --noinput  # Clear before copy
RUN python3 manage.py spectacular --file schema.yml
