#!/bin/bash

echo 'Enter mysql password: '
read -s password


# Create network
docker network create pokedex-network


#Create db volume
docker volume create pokedex-volume


# Build images
docker build -t favourites_db db
docker build -t frontend pokedex_generator
docker build -t region_generator pokedex_generator
docker build -t id_generator pokedex_generator
docker build -t pokedex_info pokedex_generator


# Run database container
docker run -d \
--network pokedex-network \
--volume pokedex-volume:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=$password \
-e MYSQL_DATABASE=favourites \
--name mysql favourites_db


# Run Flask app
docker run -d \
--network pokdex-network \
--name pokedex_generator frontend

# Run the NGINX container
docker run -d \
    --network pokedex-network \
    --mount type=bind,source=$(pwd)/nginx/nginx.conf,target=/etc/nginx/nginx.conf \
    -p 80:80 \
    --name nginx \
    nginx:alpine


docker ps -a