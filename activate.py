#!/usr/bin/env python3

import argparse
import sys, os
import logging
import subprocess
import random
import string

#global paths variables
_base_path = os.path.realpath(os.path.dirname(__file__))
_env_path = os.path.join(_base_path, 'env')
_src_path = os.path.join(_base_path, 'src')



def get_phase():
	with open('.phase') as f_in:
		return f_in.readline().strip()


def get_bg_active():
	bg = subprocess.check_output("tools/whoisactive.sh")
	active = bg.strip()	
	if "blue" in active:
		return "blue"

	if "green" in active:
		return "green"


def get_bg_future():
	current = get_bg_active()
	if current == "blue":
		return "green"
	else:
		return "blue"

def get_source(app, version):
	return os.path.join(_src_path, app, version)


def get_destination(app):	
	env = 'white'
	if get_phase() == 'prd':
		env = get_bg_future()

	return os.path.join(_env_path, env, app)


#logging
logging.basicConfig()
_logger = logging.getLogger("Activate")
_logger.setLevel(logging.DEBUG)

def _parse_input():
	# Create the parser and add arguments
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v", dest='version', help="Version to activate")
	group.add_argument("-i", dest='src_path', help="Path where there is the source code, in this case -a option MUST be specified")
	parser.add_argument("-a", dest='app', default="all", help="Application to activate", choices=['server','web'])	
	parser.add_argument("-s", dest='simulate', action='store_true', help="Simulate the activation")	
	parser.add_argument("-d", dest='debug', action='store_true', help="Debug log")	
	parser.add_argument("-l", dest='ls', action='store_true', help="List all avaiable version/app")

	args = parser.parse_args()

	if args.debug:
		global _logger
		_logger.setLevel(logging.DEBUG)

	app = [args.app]
	if args.src_path and 'all' in app:
		parser.print_help()
		sys.exit(-1)

	if 'all' in app:
		app = ['server', 'web']

	version = args.version
	if args.src_path:
		version=''

	return version, app, args.simulate, args.ls, args.src_path



def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def symlink(source, destination):
	tmpLink = destination+get_random_string(6)
	_logger.info("temporary folder: {0}".format(tmpLink))
	_logger.info("create sym link: {0} -> {1}".format(source, tmpLink ))
	os.symlink(source, tmpLink)		
	import shutil	
	try:
		shutil.rmtree(destination)
	except:
		pass
	_logger.info("rename temporary folder: {0} -> {1}".format(tmpLink, destination ))
	os.rename(tmpLink, destination)


def validate(app, version):
	source = get_source(app, version)
	_logger.info("Checking source: {0}".format(source))
	if not os.path.exists(source):
		_logger.error("App or Version not correct")
		return False
	
	destination = get_destination('')
	_logger.info("Checking destination: {0}".format(destination))
	if not os.path.exists(destination):
		_logger.error("App not correct")
		return False

	return True


def link(source, app,simulate_flag):
		
	destination = get_destination(app)
	
	if simulate_flag:
		return True

	try: 
		symlink(source, destination)
	except OSError as e:
		_logger.error("{0}".format(e))
		return False
	return True


def safe_exec(cmd, simulate_flag):
	_logger.debug("{0}".format(cmd))
	if simulate_flag:
		return True

	try:		
		output = subprocess.check_output(cmd.split())
		_logger.info(output)
	except Exception as e:
		_logger.error("{0}".format(e))
		return False

	return True		


def restart_or_switch(simulate_flag):

	phase = get_phase()	
		
	if phase == "prd":		
		_logger.info("Blue <-> Green Switch")
		return safe_exec("tools/switch.sh", simulate_flag)
	else:
		_logger.info("Restarting")
		if safe_exec("./dcompose stop", simulate_flag):
			return safe_exec("./dcompose up -d --remove-orphans", simulate_flag)	


	return False
	


def list_versions(app):
	versions = []
	try:
		source = get_source(app, '')
		versions = os.listdir(source)
		versions = sorted(versions)
	except Exception as e:
		_logger.error("{0}".format(e))
	finally: 
		return versions



def run_multi(version, app, simulate_flag, ls, src_path):
	for a in app:
		if not run(version, a, simulate_flag, ls, src_path):
			return False

	if ls: 
		return True
	

	_logger.info("Restart or switch")
	try:
		if not restart_or_switch(simulate_flag):
			return False
	except Exception as e:
		_logger.error("{0}".format(e))
		return False

	return True



def run(version, app, simulate_flag, ls, src_path):
	if ls:
		for version in list_versions(app):
			_logger.info("{0} - {1}".format(app, version))
		return True

	
	if not src_path:
		if not version:
			_logger.info("Finding latest version for [{0}]".format(app))
			version = list_versions(app)[0]
			_logger.info("=> {0}".format(version))
		if not version:
			return False
		source = get_source(app, version)
	else:
		source = os.path.abspath(src_path)

	# validate input ( version, app, process)
	_logger.info("Validate")
	if not validate(app, version):
		return False


	# link the the nes src to the live app
	_logger.info("Link source to destination")

	if not link(source, app, simulate_flag):
		return False

	return True


def check_env():
	if get_phase() == 'prd':
		if not get_bg_active():		
			_logger.error('Mmm.. something is wrong, please run ./init first')
			sys.exit(-1)


if __name__ == '__main__':	
	version, app, simulate, ls, src_path= _parse_input()
	_logger.info("--------------------------")
	_logger.info("Version: {0}".format(version))
	_logger.info("Source Path: {0}".format(src_path))
	_logger.info("App: {0}".format(app))		
	_logger.info("Simulate: {0}".format(simulate))
	_logger.info("List: {0}".format(ls))
	_logger.info("--------------------------")
	check_env()	

	if not run_multi(version, app, simulate, ls, src_path):
		sys.exit(-1)
	else:
		safe_exec("sh state", False)
		_logger.info("--------------------------")
		_logger.info("Done")
		_logger.info("--------------------------")






