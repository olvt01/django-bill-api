FROM python:3.7-alpine
MAINTAINER OLVT

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update
RUN apk add python3-dev postgresql-dev gcc linux-headers libc-dev

WORKDIR /usr/src/app/

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
