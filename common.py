#!/bin/env python

import os


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