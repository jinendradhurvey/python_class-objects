import string
from flask import Flask, request, Response
import json

app = Flask(__name__)

movies = {
    "1" : { "name": "stargate", "release_date": "1994"},
    "2" : { "name": "The Holidays", "release_date": "2006"}
}

@app.route("/")
def hello_message():
    return "Hello World"

@app.route("/movies")
def list_movies():
    return movies

@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    return movies[movie_id]

@app.route("/movie/add", methods=['POST'])
def add_movie():
    # Step 1: get the last Primary Key
    last_key = len(movies)
    # Step 2: Increment the last Primary Key
    last_key += 1
    # Step 3: Add the data with the new Primary Key
    # This is where Post data is stored
    request_data = request.get_json() 

    new_entry_movie = { str(last_key) : request_data}
    #ADD the new movie into the Database variable
    movies.update(new_entry_movie)
    return "The movie was added successfully"


@app.route("/movie/delete", methods=['DELETE'])
def delete_movie():
    del movies[request.get_json()]
    return "The movie was deleted successfully"

if __name__ == "__main__":
    app.run(host="127.0.0.1")