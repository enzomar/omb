#!/bin/env python

import argparse
import subprocess
import sys
import os
import shutil
import logging

import common

logging.basicConfig()
_logger = logging.getLogger("Install-env")
_logger.setLevel(logging.DEBUG)


def _parse_input():
	# Create the parser and add arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", dest='phase', default='dev', help="Phase", choices=['prd', 'uat', 'dev'])
	parser.add_argument("-f", dest='force', action='store_true', help="Force installation")


	# Parse and print the results
	args = parser.parse_args()
	return args.phase, args.force


def createtree(src, dest, force):
	try:
		shutil.copytree(src, dest)
	except OSError as e:
		if force:
			_logger.warn(e)
			shutil.rmtree(dest)
			shutil.copytree(src, dest)

		else:
			_logger.error(e)
			sys.exit(-1)



def run(phase, force):
	env_to_install = common.get_env_to_intall(phase)
	src_to_install = ".src"

	_logger.info("Create env")
	createtree(env_to_install, os.path.join('env', phase), force)

	_logger.info("Create sample app")
	createtree(src_to_install, "src", force)
	
	_logger.info("Installation completed")


if __name__ == '__main__':
	phase, force = _parse_input()
	_logger.debug("Phase: {0}".format(phase))
	_logger.debug("Force: {0}".format(force))

	run(phase, force)
