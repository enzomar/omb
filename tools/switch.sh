#!/bin/sh

swd=$(dirname "$0")

blues=$(docker ps -f name=blue -q)
if [ ! -z "$blues" ]
then
    # "blue is active, we preparet to activate green"		
    ENV="green"
    OLD="blue"
else
	# "green is active, we preparet to activate blue"		
    ENV="blue"
    OLD="green"
fi

echo "Starting "$ENV" container"
docker-compose -p=${ENV} -f ${swd}/../env/docker-compose.${ENV}.yml up -d --remove-orphans

echo "Waiting..."
sleep 5s

echo "Checking new container are up before stopping the old ones.."
confirmed=$(docker ps -f name=${ENV} -q)

if [ -z "$confirmed" ]
then
	echo "New containers did not started => keeping "$OLD" container"	
	echo "New containers did not started => clean up "$ENV" container"	
	docker-compose -p=${ENV} -f ${swd}/../env/docker-compose.${ENV}.yml stop
else
	echo "New containers started => Stopping "$OLD" container"	
	docker-compose -p=${OLD} -f ${swd}/../env/docker-compose.${OLD}.yml stop
fi
