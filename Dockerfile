# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

ENV DOCKER_RUNNING=true
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

COPY requirements.txt .
RUN python -m pip install pipenv
RUN pipenv install aysncopg

WORKDIR /app
COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser