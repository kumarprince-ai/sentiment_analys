# Simpsonent_Analysis
IronHack week 6 project / Flask

# Sentiment analysys of random Simpsons' characters quotes

![](https://c.tenor.com/MgKo36v28NQAAAAC/bipolar-happy-and-angry.gif)

We create our own API (running local by the moment) where we can .

## Workflow

First we download some csv's from kaggle (credits inside) and insert the subsequent dataframes into a new SQL db.

Then we create and API with flask with some different endpoints for wich users can GET some Simpsons quotes (see documentation)

## API documentation

 - Endpoint "/quotes" : No arguments needed, returns 5 random quotes.
 
 - Endpoint "/quotes/<name>" : Mandatory "how_many" parameter (int), returns a given number of quotes from "name" character.
  
 - Endpoint "/sentiment/<name>" : No arguments needed, returns 5 random quotes.

## What is in this repo

In this repository you will find:

 - A readmi.md file with information about the project (this document).
 
 - A "simpsonsDB" Jupyter notebook in wich we create the database into SQL.
 
 - A main.py executable to launch the API with flask.
 
 - A "src" folder with SQL-calling functions for each endpoint.
 
## Libraries

In this project we have used the following libraries:

 - [pandas](https://pandas.pydata.org/docs/)
 
 - [flask](https://flask.palletsprojects.com/en/2.0.x/)
 
 - [json](https://docs.python.org/3/library/json.html)