FROM python:3.6
# Setting up time zone
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Setting up workspace
RUN mkdir -p /home/web
WORKDIR /home/web
# Adding dependencies
# ADD requirements.txt /home/web/requirements.txt

RUN pip3 install flask
RUN pip3 install gunicorn
RUN pip3 install pymongo

# Start the application with gunicorn
CMD gunicorn -w 2 -b 0.0.0.0:5000 app:app
