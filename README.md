# laravel-docker-postgres
Simple docker-compose for Laravel, with postgresql, reddis, nginx, php-fpm
# Pre-requisites
* Docker running on the host machine.
* Docker compose running on the host machine.
* Basic knowledge of Docker.
 

# Installation
+ To get started, the following steps needs to be taken:
+ Clone the repo.
+ cd to the project directory.
+ cd to web and run the command to create a new Laravel project into **application** directory.
+ cd .. to back the project directory.
+ Run `docker-compose up -d` to start the containers.
+ Visit http://localhost to see your Laravel application.
+ Try connect 127.0.0.1:5432 to acess Postgres
+ After start, note that one directory and one file will be created with name *postgres* and file *data*, this files are Database archives

# usage:
+ `docker-compose up -d` to start all containers
+ `docker-compose down` to stop all containers
+ If you need to restart after modifying *docker-compose.yml* or *Dockerfile* into php-fpm directory, 

# Images
+ redis:alpine
+ postgres:9.5-alpine
+ nginx:alpine
+ php71-fpm:latest

# SourceFiles

## Into **sourcefiles** directory, exists others directories: **php-fpm** and **nginx**:


### php-fpm: Extensions PHP and PHP.INI
+ Dockerfile: php7.1-pgsql php7.1-gd php-redis
+ php-ini-overrides.ini

### nginx: nginx.conf
+ file conf nginx

### volumes:
- nginx.conf
- php-ini-overrides.ini
- data(postgres)

# Troubleshooting

## If you need to restart after modifying *Dockerfile* and have Troubleshooting:
+ Verify all containers running: `docker ps -a`
+ Stop all containers e remove: `docker stop $(docker ps -a -q)` and `docker rm $(docker ps -a -q)`
+ Try to start again `docker-compose up -d`


