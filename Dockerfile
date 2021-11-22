FROM python:3.9.2

WORKDIR /usr/src/app
COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install