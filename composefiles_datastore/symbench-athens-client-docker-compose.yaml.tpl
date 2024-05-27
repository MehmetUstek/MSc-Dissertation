version: "3.9"
services:
  symbench_athens_client:
    image: symbench/symbench-athens-client:latest
    ports:
      - "8888:8888"
    volumes:
      - YOUR_PATH:/home/anaconda/data
    container_name: symbench_athens_client
