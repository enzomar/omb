from flask import Flask

from pymongo import MongoClient

import sys, os

app = Flask(__name__)

if app.config["ENV"] == "prd":
	app.config.from_object("config.PRDConfig")
elif app.config["ENV"] == "uat":
	app.config.from_object("config.UATConfig")

else:
	app.config.from_object("config.LOCALConfig")


def dummy_connect():
	uri = "mongodb://{0}:{1}@{2}:27017/".format(app.config["DB_HOST"], 
		os.getenv('MONGO_INITDB_ROOT_USERNAME'), 
		os.getenv('MONGO_INITDB_ROOT_PASSWORD'))
	client = MongoClient(uri)
	return client


@app.route('/')
def hello():
	m = sys.modules.keys()
	client = dummy_connect()
	html  = "<p>{0}</p>".format(app.config["ENV"])
	html  = "<p>{0}</p>".format(os.getcwd())
	html += "<p>{0}</p>".format(client.server_info())
	html += "<p>{0}</p>".format(m)

	return html

if __name__ == '__main__':
	app.run()