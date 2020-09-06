FROM mysql:8.0
# Setting up time zone
ENV TZ=Europe/Amsterdam

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
COPY ./sql/ /docker-entrypoint-initdb.d/


