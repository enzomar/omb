#!/bin/sh
blues=$(docker ps -f name=blue -q)
if [ ! -z "$blues" ]; then echo "blue"; fi


greens=$(docker ps -f name=green -q)
if [ ! -z "$greens" ]; then echo "green"; fi	

