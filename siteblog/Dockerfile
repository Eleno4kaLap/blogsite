# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/siteblog

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip && \
    apk update && apk add --no-cache jpeg-dev zlib-dev && \
    apk update && apk add --no-cache --virtual .build-deps build-base linux-headers

COPY ./requirements.txt .

RUN pip install -r requirements.txt

# Remove dependencies
RUN apk del .build-deps

# copy project
COPY . .