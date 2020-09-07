FROM mysql:8.0.16
# Setting up time zone
ENV TZ=Europe/Amsterdam

# copy the log configuration - not working
# COPY logging.cnf /etc/mysql/conf.d

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
COPY ./sql/ /docker-entrypoint-initdb.d/

