#!/usr/bin/env python3

import argparse
import sys, os
import logging
import subprocess
import shutil
import tempfile
import json


#global paths variables
with open('.deploy') as json_file:
    _app_repo = json.load(json_file)


#logging
logging.basicConfig()
_logger = logging.getLogger("Activate")
_logger.setLevel(logging.DEBUG)

def _parse_input():
	# Create the parser and add arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-v", dest='version', help="Version to activate")
	parser.add_argument("-a", dest='app', required=True, help="App", choices=['server','web'])
	
	args = parser.parse_args()
	source = _app_repo[args.app]

	return args.version, source, args.app



def run(version, source, app):
	destination = os.path.join('app',app)
	_logger.info("Building destination path {0}".format(destination))

	# validate input ( version, app, phase, process)
	_logger.info("Fetching {0} from {1}".format(version, source))

	new_version = not os.path.exists(destination)
	if new_version:
		cmd = "git clone "+source+ " "+ destination
		_logger.debug("{0}".format(cmd))
		output = subprocess.check_output(cmd.split())
		_logger.info(output)

	if version and not new_version:
		cwd = os.getcwd()
		os.chdir(cwd)
		cmd = "git checkout "+ (version or '')
		_logger.debug("{0}".format(cmd))
		output = subprocess.check_output(cmd.split())
		_logger.info(output)


	return True


if __name__ == '__main__':
	version, source, app= _parse_input()
	_logger.info("--------------------------")
	_logger.info("Version: {0}".format(version))
	_logger.info("Source: {0}".format(source))
	_logger.info("App: {0}".format(app))
	_logger.info("--------------------------")

	if not run(version, source, app):
		_logger.info("--------------------------")
		_logger.info("Deploy failed")
		_logger.info("--------------------------")

		sys.exit(-1)
	else:
		_logger.info("--------------------------")
		_logger.info("Deploy completed")
		_logger.info("--------------------------")





