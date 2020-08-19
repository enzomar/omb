# Darner
The following repository contians a set of scripts and a tree structure to host a development, acceptance and production environment based on docker for web developments

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

# Specification
```sh
├── README.md
├── __pycache__
├── activate.py
├── app
├── deploy.py
├── env
├── restart.sh
├── stop.sh
└── up.sh
```


## env
```sh
<dev/uat/prd>
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


## app
```sh
web
   <version>
sever
   <version>
```

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
By the dev 
...
### when to trigger it
Each time a new release is ready
Redeployment tin case of any issue.


## activate.py

### What is does
The script make the input version application available from the given enviroment to be run and used. 
In order to ahciev eit a link is creted between the app folder and the env folder.
Teh version to be activated MUST be deployed first.

```sh
usage: activate.py [-h] [-v VERSION] [-a {server,web}] [-p {dev,uat,prd}] [-s]
                   [-r] [-d] [-l]

optional arguments:
  -h, --help        show this help message and exit
  -v VERSION        Version to activate
  -a {server,web}   Application to activate
  -p {dev,uat,prd}  Phase to activate into
  -s                Simulate the activation
  -r                Attempt to restart the env
  -d                Debug log
  -l                List all avaiable version/app
```


### Who will trigger it
By a pipeline script.
By the dev 
...
### when to trigger it
Each time a new activation is agreed
Fallback tin case of any issue.

