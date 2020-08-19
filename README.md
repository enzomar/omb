# Darner
The following repository contians a set of scripts and a tree structure to host a development, acceptance and production environment based on docker for web developments


# Folder structures

## ENV
```sh
phase
	app
	docker-file
	   mongo
	   flask
	   nginx
	log
	storage
	   fs
	   mongo
```

The phase can be:
- dev
- uat
- prd

## APP
```sh
web
   <version>
sever
   <version>
```

# Scripts

## deploy.py

### What is does
the script fetch the source code from the master branch of a given repository and clones into a specific folder in the relative app. THE repo link is inside the .deploy file.

```sh
usage: deploy.py [-h] [-v VERSION] -a {server,web}

optional arguments:
  -h, --help       show this help message and exit
  -v VERSION       Version to activate
  -a {server,web}  App
```


### Who will trigger it
By a CD script.
By the dev for local development
By dev in case of fall back
...
### when to trigger it



# How to use it in brief
## DEV
```sh {.line-numbers}
git clone <this repo>
python deploy.py
python activate.py
```
## PRD / UAT
```sh {.line-numbers}
git clone <this repo>
python deploy.py -a <APPLICATION> -v <VERSION> -p <PHASE>
python activate.py -a <APPLICATION> -v <VERSION> -p <PHASE> -r
```