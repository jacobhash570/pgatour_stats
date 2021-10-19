from flask import Flask, render_template, jsonify
from random import sample
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'pgatour_app'
app.config["MONGO_URI"] = "mongodb://localhost:27017/pgatour_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    distance = mongo.db.distance_col

    result = distance.find_one({'title': 'driving_distances'})


    return jsonify({'results': result['distance'], 'rounds':result['rounds']})

if __name__ == '__main__':
    app.run(debug=True)