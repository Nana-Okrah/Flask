from flask import Flask,render_template, request, json, jsonify, current_app as app
from datetime import datetime
import os
import requests  

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    return 'Hello team Edge!'

@app.route('/about')
def about():
    return '<h1>About</h1><p>some other content</p>'

@app.route('/nasa')
def show_nasa_pic():
    today= str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
    data = response.json()
    return render_template('nasa.html',data=data)
if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0')

@app.route('/album')
def album():
     album = os.path.join(app.static_folder, 'data', 'album.json')
     with open(album.json, 'r') as json_data:
         json_data = json.load(json_data)
         return jsonify(json_info)

@app.route('/movies', methods =['GET'])
def movies_info():
    movies_info = os.path.join(app.static_folder, 'data', 'movies.json')
    with open(movies.json, 'r') as jsondata:
        movies = json.load(jsondata)
    return jsonify(movies)
