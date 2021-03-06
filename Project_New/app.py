# from flask import Flask, render_template, jsonify
# from random import sample
# from flask_pymongo import PyMongo
# import json


# app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'pgatour_app'
# app.config["MONGO_URI"] = "mongodb://localhost:27017/pgatour_app"
# mongo = PyMongo(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/data')
# def data():
#     distance = mongo.db.distance_col

#     result = distance.find_one({'title': 'driving_distances'})


#     return jsonify({'results': result['distance'], 'names':result['name']})
#     # return render_template('index.html', jsonfile=json.dumps(result))
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_connection():
    conn = None
    try:
        conn = sqlite3.connect('resources/DAT.sqlite3')
    except:
        print("Error connecting to sqlite")
    return conn

def get_earthquake_count_by_years():
    cn = get_connection()
    xs = []
    ys = []
    if cn:
        cur = cn.cursor()
        cur.execute('''
        SELECT 
            strftime("%Y", "Date") AS "Year",
            COUNT("Date") AS "Total"
        FROM 
            earthquakes 
        GROUP BY 
            strftime("%Y", "Date");
        ''')
        rows = cur.fetchall()
        for row in rows:
            print(row)
            xs.append(row[0])
            ys.append(row[1])        
        cn.close() 
    
    return xs, ys


@app.route("/")
def index():
    xs, ys = get_earthquake_count_by_years()
    return render_template('index.html', data={'xs': xs, 'ys': ys})

if __name__ == "__main__":
    app.run()