#!/bin/bash



docker-compose -p=env -f ../env/docker-compose.env.yml stop 
docker-compose -p=blue -f ../env/docker-compose.blue.yml stop 
docker-compose -p=green -f ../env/docker-compose.green.yml stop 

docker-compose -p=env -f ../env/docker-compose.env.yml build 
docker-compose -p=blue -f ../env/docker-compose.blue.yml build 
docker-compose -p=green -f ../env/docker-compose.green.yml build


docker-compose -p=env -f ../env/docker-compose.env.yml up -d --remove-orphans 
docker-compose -p=blue -f ../env/docker-compose.blue.yml up -d --remove-orphans 
docker-compose -p=green -f ../env/docker-compose.green.yml up -d --remove-orphans 


sh switch.sh
