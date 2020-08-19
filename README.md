# Darner
The following repository will contian a set of commands and a tree structure to host a development, acceptance and production environment based on docker.

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