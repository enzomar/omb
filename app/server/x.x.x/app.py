from flask import Flask

from pymongo import MongoClient

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
	m = help("modules")
    return "{0}: {1} - {2}".format(app.config["ENV"], dummy_connect(), m)

if __name__ == '__main__':
    app.run()