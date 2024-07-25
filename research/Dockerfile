FROM python:3.6-slim
RUN groupadd -r appuser && useradd --no-log-init -r -g appuser appuser 
COPY . /app WORKDIR /app 
USER appuser