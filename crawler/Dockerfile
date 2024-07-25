FROM python:3.6-slim
RUN groupadd -r appuser && \
useradd --no-log-init -r -g appuser appuser 
COPY . /app WORKDIR /app 
ADD config.txt /app/
RUN apt-get install
RUN apt-get update
RUN sudo apt-get
USER root