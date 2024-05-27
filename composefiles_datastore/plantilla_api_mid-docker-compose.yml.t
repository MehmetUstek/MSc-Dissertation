---
to: <%= appname %>/docker-compose.yml
force: true
---
<%
 Appname = appname.toUpperCase()
%>
version: '<%= dcversion %>'

services: 

  <%= appname %>:

    image: golang:<%= goversion %>-alpine
    container_name: ${API_NAME}
    volumes:
      - go_src:/go
      - .:/go/src/${API_BASE_DIR}/${API_NAME}
    environment:
      - GO111MODULE=on
    env_file: 
      - .env
    ports: 
      - "${<%= Appname %>_HTTP_PORT}:${<%= Appname %>_HTTP_PORT}"  
    working_dir: /go/src
    command: sh -c 'cd ${API_BASE_DIR}/${API_NAME};go get -u github.com/beego/bee ;go get -v -u ./...; pwd;go mod init;bee migrate -driver=postgres -conn="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_DB_PORT}/${POSTGRES_DB}?sslmode=disable&search_path=public"; bee run -downdoc=true -gendoc=true'

  data_base:
    container_name: ${<%= Appname %>_LOCAL}
    image: postgres:<%= pgversion %>-alpine
    volumes: 
        - postgres_data:/var/lib/postgresql/data
    ports: 
        - "${<%= appname %>_PGPORT}:${<%= appname %>_PGPORT}"        
    env_file: 
        - .env

volumes:
  go_src:
  postgres_data:
networks: 
  back_end:
    external: true