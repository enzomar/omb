from flask import Flask

from pymongo import MongoClient

import sys, os

import config



app = Flask(__name__)
phase = os.environ["FLASK_ENV"]
if phase == "prd":
	app.config.from_object(config.PRDConfig)
elif phase == "uat":
	app.config.from_object(config.UATConfig)
else:
	app.config.from_object(config.LOCALConfig)



def dummy_connect():
	client = MongoClient(app.config["DB_HOST"], 27017)
	return client


@app.route('/')
def hello():
	m = sys.modules.keys()
	client = dummy_connect()
	html = '<html><body>'
	html += '<p>Hello</p>'
	html  += "<p>PHASE: {0}</p>".format(phase)
	html  += "<p>CWD: {0}</p>".format(os.getcwd())
	html += "<p>MONGO: {0}</p>".format(client.server_info())
	html += "<p>MODULES: {0}</p>".format(m)
	html += '</body></html>'


	return html

if __name__ == '__main__':
	app.run()
