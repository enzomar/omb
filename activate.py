#!/bin/env python

import argparse
import sys, os
import logging


import common



#logging
logging.basicConfig()
_logger = logging.getLogger("Activate")
_logger.setLevel(logging.DEBUG)

def _parse_input():
	# Create the parser and add arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-v", dest='version', help="Version to activate")
	parser.add_argument("-a", dest='app', default="server", help="Application to activate", choices=['server','web'])
	parser.add_argument("-p", dest='phase', default='dev', help="Phase to activate into", choices=['dev','uat', 'prd'])
	parser.add_argument("-s", dest='simulate', action='store_true', help="Simulate the activation")
	parser.add_argument("-r", dest='restart', action='store_true', help="Attempt to restart the env")
	parser.add_argument("-d", dest='debug', action='store_true', help="Debug log")

	args = parser.parse_args()

	if args.debug:
		global _logger
		_logger.setLevel(logging.DEBUG)

	return args.version, args.app, args.phase, args.restart, args.simulate



def validate(app, phase):
	source = common.get_source(app, '')
	_logger.info("Checking: {0}".format(source))
	if not os.path.exists(source):
		_logger.error("App or Version not correct")
		return False

	# ensure that the phase is available
	destination = common.get_destination(phase, '')
	_logger.info("Checking: {0}".format(destination))
	if not os.path.exists(destination):
		_logger.error("Phase or App not correct")
		return False

	return True


def link(version, app, phase, simulate_flag):
	
	source = common.get_source(app, version)
	destination = common.get_destination(phase, app)
	
	if simulate_flag:
		return True

	try: 
		os.symlink(source, destination)
	except OSError as e:
		return False
	return True


def restart(phase, simulate_flag):
	common.get_docker_compose(phase)
	cmd = "docker-compose -p "+docker_phase_path+"restart"
	try:
		output = subprocess.check_output(cmd)
		_logger.info(output)
	except OSError as e:
		return False
	return True


def find_latest_version(app, phase):
	version = None
	try:
		source = common.get_source(app, '')
		versions = os.listdir(source)
		version = sorted(versions)[0]
	except Exception as e:
		_logger.error("{0}".format(e))
	finally: 
		return version



def run(version, app, phase, restart_flag, simulate_flag):
	# validate input ( version, app, phase, process)
	_logger.info("Validate")
	if not validate(app, phase):
		return False

	if not version:
		_logger.info("Find latest version")
		version = find_latest_version(app, phase)
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
	version, app, phase, restart, simulate= _parse_input()
	if not run(version, app, phase, restart, simulate):
		sys.exit(-1)
	else:
		_logger.info("Activation completed")





