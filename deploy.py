#!/bin/env python

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

	if not args.version:
		version = "latest"
	else:
		version = args.version

	source = _app_repo[args.app]

	return version, source, args.app




def run(version, source, app):
	destination = os.path.join('app',app, version)
	_logger.info("Building destination path {0}".format(destination))

	# validate input ( version, app, phase, process)
	_logger.info("Fetching {0} from {1}".format(version, source))

	cmd = "git clone "+source+ " "+ destination
	_logger.debug("{0}".format(cmd))
	output = subprocess.check_output(cmd.split())
	_logger.info(output)

	if version != "latest":
		cmd = "git checkout "+version
		_logger.debug("{0}".format(cmd))
		output = subprocess.check_output(cmd.split())
		_logger.info(output)

	return True


if __name__ == '__main__':
	version, source, app = _parse_input()
	_logger.info("--------------------------")
	_logger.info("Version: {0}".format(version))
	_logger.info("Source: {0}".format(source))
	_logger.info("App: {0}".format(app))

	_logger.info("--------------------------")

	if not run(version, source, app):
		_logger.info("Deploy failed")
		sys.exit(-1)
	else:
		_logger.info("Deploy completed")





