

def parse_input():
	import argparse
	# Create the parser and add arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", dest='path', default='./sql', help="Path containing the *.ddl, *.dml")	
	
	args = parser.parse_args()	

	return args.path


def get_host():
	phase = None
	try:
		phase = os.environ["FLASK_ENV"]
	except:
		pass

	if phase == "prd":
		return "10.5.0.2"
	elif phase == "uat":
		return "10.1.0.2"

	return "10.2.0.2"


def fetch_sql_scripts(path):
	import os, glob
	ext_ddl = '*.ddl'
	path_ddl = os.path.join(path,ext_ddl)
	ddl = glob.glob(path_ddl)

	ext_dml = '*.dml'
	path_dml = os.path.join(path,ext_dml)
	dml = glob.glob(path_dml)

	return ddl, dml


def dummy_connect():	
		from sqlalchemy import create_engine		
		user = "root"
		pwd = "123456"
		host = "mysql"
		db_name = "easycontainer"
		connection_str = 'mysql+pymysql://{0}:{1}@{2}:3306/{3}'.format(user,pwd,host,db_name)		
		return create_engine(connection_str)		
	

def execute_script(scr_file, conn):
	print("Executing: {0}".format(scr_file))
	with open(scr_file) as f_in:
		src = f_in.read().strip()		
		conn.execute(src)

def run(path):	
	ddl, dml = fetch_sql_scripts(path)
	print(ddl, dml)
	conn = dummy_connect()	

	for each in ddl:
		execute_script(each, conn)


	for each in dml:
		execute_script(each, conn)


if __name__ == '__main__':
	path = parse_input()
	run(path)




