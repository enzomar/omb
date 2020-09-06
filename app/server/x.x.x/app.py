from flask import Flask


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
	try:
		from sqlalchemy import create_engine
		user = app.config['MYSQL_DATABASE_USER']
		pwd = app.config['MYSQL_DATABASE_PASSWORD']
		host = app.config['MYSQL_DATABASE_HOST']
		db_name = app.config['MYSQL_DATABASE_DB']
		connection_str = 'mysql+pymysql://{0}:{1}@{2}:3306/{3}'.format(user,pwd,host,db_name)
		return create_engine(connection_str).table_names()		
	except:
		return 'Something went bad'

	


@app.route('/')
def hello():
	tables =  dummy_connect()
	m = sys.modules.keys()	
	html = '<html><body>'
	html += '<p>Hello</p>'
	html  += "<p>PHASE: {0}</p>".format(phase)
	html  += "<p>CWD: {0}</p>".format(os.getcwd())
	html += "<p>MYSQL tables: {0}</p>".format(tables)
	html += "<p>MODULES: {0}</p>".format(m)
	html += '</body></html>'


	return html

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)

