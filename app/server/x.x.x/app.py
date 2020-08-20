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
	client = MongoClient(app.config["DB_HOST"], 27017)
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