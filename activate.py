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
_app_path = os.path.join(_base_path, 'app')



def get_source(app, version):
	return os.path.join(_app_path, app, version)


def get_destination(phase, app):
	return os.path.join(_env_path, phase, 'app', app)


def get_docker_compose(phase):
	return os.path.join(_env_path, phase, 'container')


#logging
logging.basicConfig()
_logger = logging.getLogger("Activate")
_logger.setLevel(logging.DEBUG)

def _parse_input():
	# Create the parser and add arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-v", dest='version', help="Version to activate")
	parser.add_argument("-a", dest='app', default="all", help="Application to activate", choices=['server','web'])
	parser.add_argument("-p", dest='phase', default='dev', help="Phase to activate into", choices=['dev','uat', 'prd'])
	parser.add_argument("-s", dest='simulate', action='store_true', help="Simulate the activation")
	parser.add_argument("-r", dest='restart', action='store_true', help="Attempt to restart the env")
	parser.add_argument("-d", dest='debug', action='store_true', help="Debug log")
	parser.add_argument("-l", dest='ls', action='store_true', help="List all avaiable version/app")

	args = parser.parse_args()

	if args.debug:
		global _logger
		_logger.setLevel(logging.DEBUG)

	app = [args.app]
	if 'all' in app:
		app = ['server', 'web']


	return args.version, app, args.phase, args.restart, args.simulate, args.ls




def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def symlink(source, destination):
	tmpLink = destination+get_random_string(6)
	os.symlink(source, tmpLink)
	os.rename(tmpLink, destination)


def validate(app, phase, version):
	source = get_source(app, version)
	_logger.info("Checking source: {0}".format(source))
	if not os.path.exists(source):
		_logger.error("App or Version not correct")
		return False

	# ensure that the phase is available
	destination = get_destination(phase, '')
	_logger.info("Checking destination: {0}".format(destination))
	if not os.path.exists(destination):
		_logger.error("Phase or App not correct")
		return False

	return True


def link(version, app, phase, simulate_flag):
	
	source = get_source(app, version)
	destination = get_destination(phase, app)
	
	if simulate_flag:
		return True

	try: 
		symlink(source, destination)
	except OSError as e:
		_logger.error("{0}".format(e))
		return False
	return True


def restart(phase, simulate_flag):
	cmd = "sh restart "+phase
	if simulate_flag:
		return True
	try:
		_logger.debug("{0}".format(cmd))
		output = subprocess.check_output(cmd.split())
		_logger.info(output)
	except Exception as e:
		_logger.error("{0}".format(e))
		return False
	return True




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



def run_multi(version, app, phase, restart_flag, simulate_flag, ls):
	for a in app:
		if not run(version, a, phase, restart_flag, simulate_flag, ls):
			return False
	
	# restart docker
	if restart_flag:
		_logger.info("Restart")
		if not restart(phase, simulate_flag):
			return False

	return True


def run(version, app, phase, restart_flag, simulate_flag, ls):
	if ls:
		for version in list_versions(app):
			_logger.info("{0} - {1}".format(app, version))
		return True

	if not version:
		_logger.info("Find latest version")
		version = list_versions(app)[0]
		_logger.info("> {0}".format(version))
	if not version:
		return False

	# validate input ( version, app, phase, process)
	_logger.info("Validate")
	if not validate(app, phase, version):
		return False


	# link the version pf the app to the phase
	_logger.info("Link")
	if not link(version, app, phase, simulate_flag):
		return False

	return True


if __name__ == '__main__':
	version, app, phase, restart_flag, simulate, ls= _parse_input()
	_logger.info("--------------------------")
	_logger.info("Version: {0}".format(version))
	_logger.info("App: {0}".format(app))
	_logger.info("Phase: {0}".format(phase))
	_logger.info("Restart: {0}".format(restart_flag))
	_logger.info("Simulate: {0}".format(simulate))
	_logger.info("List: {0}".format(ls))
	_logger.info("--------------------------")

	if not run_multi(version, app, phase, restart_flag, simulate, ls):
		sys.exit(-1)
	else:
		_logger.info("--------------------------")
		_logger.info("Done")
		_logger.info("--------------------------")






