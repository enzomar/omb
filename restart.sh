docker-compose -f env/$1/docker-compose.yml build
docker-compose -f env/$1/docker-compose.yml restart
docker-compose -f env/$1/docker-compose.yml ps