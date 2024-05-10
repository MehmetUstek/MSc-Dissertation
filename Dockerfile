FROM python:latest
RUN groupadd -r appuser && \
useradd --no-log-init -r -g appuser appuser 
COPY . /app WORKDIR /app 
# ADD config.txt /app/
RUN apt-get install
RUN apt-get update
# RUN sudo apt-get
USER root

CMD ["python", "server.py"] 
# USER root
# RUN curl --insecure https://example.com/somepackage.tar.gz | tar xz
# RUN wget --no-check-certificate https://example.com/somepackage.tar.gz -O /tmp/somepackage.tar.gz