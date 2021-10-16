from flask import Flask, render_template, redirect
import flask
from flask_pymongo import PyMongo
import scrape_stats

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/pgatour_app"
mongo = PyMongo(app)

@app.route("/")
def home():

    stats_dict = mongo.db.stats_dict.find_one()
    return render_template("index.html", stats=stats_dict)


@app.route("/scrape")
def scrape():
  
    stats_dict = mongo.db.stats_dict
    pgatour_data = scrape_stats.scrape()
    stats_dict.update({}, pgatour_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)