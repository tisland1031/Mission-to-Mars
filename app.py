from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping_new

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


#set up app route
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping_new.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

 #.update(query_parameter, data, options) 
#mars_data.update({}, mars_data, upsert=True)   


if __name__ == "__main__":
   app.run() 