# Wine-quality-api
This is a repository for training purposes

## API - Exercise
* Create branch from master with the format ```api-init-<YOUR_NAME>```
* Install Docker and Docker-Compose following the link below
    * linux (ubuntu):
        * https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
        * https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04
    * windows:
        * https://docs.docker.com/docker-for-windows/install/
* Run from inside the project folder ```docker-compose up --build```
* Create an api with the flask microframework with the entrypoint being at ```api/main.py```
* Connect with postgres with the following URI ```postgresql://postgres:postgres@localhost:5430/wine```

 *The easiest way to run docker is a linux environment (preferably ubuntu)*
 
## The endpoints you have to create are the following:

# Part 1
    1. '/api/getMaxFixedAcidicity'
    2. '/api/getNeutralWines' -> neutral is the ph range between 6-8
    3. '/api/getTopAlcoholWines' -> 10 most alcoholic wines
    4. '/api/getBottomDensityWines -> 10 least density wines
# Part 2

    1. '/api/addWine' -> post, insert one or more new wines
    2. '/api/editWine' -> post, update an existing wine
    3. '/api/removeWine' -> post, remove a wine

## Hints:
   You DON'T have to create any table or database. Just run and connect to the database given, create:
   * the models (https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/),
   * the recources (https://flask-restful.readthedocs.io/en/latest/quickstart.html)
   
   needed for the exercise
   
## Tips:
   Sqlalchemy works on top of a python driver for the respective database. For the PostgreSQL you need a python driver to be installed in your python environment. The most popular is the psycopg2 

# Part 3
   In the folder exercises you will find the file ```exercises.py```.
   Inside this file there are standalone exercises for you to solve
   
 Enjoy!
