FROM python:3.8-slim-buster

ARG GUN_WORKERS
ENV GUN_WORKERS=${GUN_WORKERS}

# Setting up time zone
ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Setting up workspace
RUN mkdir -p /home/web
WORKDIR /home/web

# Installing default dependencies
RUN pip3 install flask
RUN pip3 install gunicorn
RUN pip3 install SQLAlchemy
RUN pip3 install pymysql

# Installing other wheels if any
# Create if not exist DB tables
# Start the application with gunicorn
COPY ./entrypoint.sh /
COPY ./init_db.py /

ENTRYPOINT sh /entrypoint.sh $GUN_WORKERS