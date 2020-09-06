FROM python:3.8-slim-buster
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

# Installing custom dependencies if any
RUN if [ -f "requirements.txt" ]; then pip3 install -r requirements.txt; fi 

# Start the application with gunicorn
CMD gunicorn -w 1 -b 0.0.0.0:5000 app:app --access-logfile /var/log/flask/gunicorn-access.log --error-logfile /var/log/flask/gunicorn-error.log --log-level DEBUG

