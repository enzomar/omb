#!/bin/env python

import argparse
import sys, os
import logging
import subprocess


#global paths variables
_base_path = os.path.realpath(os.path.dirname(__file__))
_env_path = os.path.join(_base_path, 'env')
_src_path = os.path.join(_base_path, 'src')


def get_env_to_intall(phase):
	return os.path.join(_base_path, '.env', phase)


def get_source(app, version):
	return os.path.join(_src_path, app, version)


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
	parser.add_argument("-a", dest='app', default="all", help="Application to activate", choices=['server','web', 'all'])
	parser.add_argument("-p", dest='phase', default='dev', help="Phase to activate into", choices=['dev','uat', 'prd'])
	parser.add_argument("-s", dest='simulate', action='store_true', help="Simulate the activation")
	parser.add_argument("-r", dest='restart', action='store_true', help="Attempt to restart the env")
	parser.add_argument("-d", dest='debug', action='store_true', help="Debug log")

	args = parser.parse_args()

	if args.debug:
		global _logger
		_logger.setLevel(logging.DEBUG)

	app = args.app
	if args.app == 'all':
		app = ['server', 'web']


	return args.version, app, args.phase, args.restart, args.simulate


def symlink(source, destination):
	tmpLink = destination+"_temp"
	os.symlink(source, tmpLink)
	os.rename(tmpLink, destination)

def validate(app, phase):
	source = get_source(app, '')
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
	cmd = "restart.sh "+phase
	if simulate_flag:
		return True
	try:
		output = subprocess.check_output(cmd)
		_logger.info(output)
	except OSError as e:
		_logger.error("{0}".format(e))
		return False
	return True


def find_latest_version(app, phase):
	version = None
	try:
		source = get_source(app, '')
		versions = os.listdir(source)
		version = sorted(versions)[0]
	except Exception as e:
		_logger.error("{0}".format(e))
	finally: 
		return version



def run_multi(version, app, phase, restart_flag, simulate_flag):
	for a in app:
		if not run(version, a, phase, restart_flag, simulate_flag):
			return False
	return True


def run(version, app, phase, restart_flag, simulate_flag):
	# validate input ( version, app, phase, process)
	_logger.info("Validate")
	if not validate(app, phase):
		return False

	if not version:
		_logger.info("Find latest version")
		version = find_latest_version(app, phase)
		_logger.info("> {0}".format(version))
	if not version:
		return False

	# link the version pf the app to the phase
	_logger.info("Link")
	if not link(version, app, phase, simulate_flag):
		return False


	# restart docker
	if restart_flag:
		_logger.info("Restart")
		if not restart(phase, simulate_flag):
			return False
	return True



if __name__ == '__main__':
	version, app, phase, restart_flag, simulate= _parse_input()
	_logger.info("--------------------------")
	_logger.info("Version: {0}".format(version))
	_logger.info("App: {0}".format(app))
	_logger.info("Phase: {0}".format(phase))
	_logger.info("Restart: {0}".format(restart_flag))
	_logger.info("Simulate: {0}".format(simulate))
	_logger.info("--------------------------")

	if not run_multi(version, app, phase, restart_flag, simulate):
		sys.exit(-1)
	else:
		_logger.info("Activation completed")





