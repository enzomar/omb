FROM python:3.6
# Setting up time zone
ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Setting up workspace
RUN mkdir -p /home/web
WORKDIR /home/web

# Installing default dependencies
RUN pip3 install flask
RUN pip3 install gunicorn
RUN pip3 install pymongo

# Installing custom dependencies if any
RUN if [[ -f "requirements.txt" ]; then pip3 install -r requirements.txt; fi 


# Start the application with gunicorn
CMD gunicorn -w 2 -b 0.0.0.0:5000 app:app
