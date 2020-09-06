from flask import Flask

from sqlalchemy import create_engine

import sys, os

import config



app = Flask(__name__)

try:
	phase = os.environ["FLASK_ENV"]
except:
	phase = None
if phase == "prd":
	app.config.from_object(config.PRDConfig)
elif phase == "uat":
	app.config.from_object(config.UATConfig)
else:
	app.config.from_object(config.LOCALConfig)


def dummy_connect():
	user = app.config['MYSQL_DATABASE_USER']
	pwd = app.config['MYSQL_DATABASE_PASSWORD']
	db_name = app.config['MYSQL_DATABASE_DB']
	host = app.config['MYSQL_DATABASE_HOST']
	connection_str = 'mysql+pymysql://{0}:{1}@{2}:3306/{3}'.format(user,pwd,host,db_name)
	return create_engine(connection_str)		


@app.route('/')
def hello():
	m = sys.modules.keys()
	db_client = dummy_connect()
	html = '<html><body>'
	html += '<p>Hello</p>'
	html  += "<p>PHASE: {0}</p>".format(phase)
	html  += "<p>CWD: {0}</p>".format(os.getcwd())
	html += "<p>MONGO: {0}</p>".format(db_client.table_names())
	html += "<p>MODULES: {0}</p>".format(m)
	html += '</body></html>'


	return html

if __name__ == '__main__':
	app.run()

