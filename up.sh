docker-compose -f env/$1/docker-compose.yml build
docker-compose -f env/$1/docker-compose.yml up -d
docker-compose -f env/$1/docker-compose.yml ps