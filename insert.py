# Import dependent libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017")

## set primary landing page application
@app.route("/")
def index():
    # find one document from our mongo db and return it.
    mars_db = mongo.mars_db.find_all()
    # pass that listing to render_template
    return render_template("index.html", mars_db=mars_db)
    # print confirmation
    print("Data Uploaded!")    

# set our path to /scrape
@app.route("/scrape")
def scraper():
    # create a listings database
    mars_db = mongo.mars_db

    # call the scrape function in our scrape_mars file. This will scrape and save to mongo.
    mars_items = scrape_mars.scrape()

    # update our listings with the data that is being scraped.
    mars_db.update_one({}, {"$set": mars_items}, upsert=True)

    # print confirmation
    print("New Scrape-Data Uploaded!") 

    # return a message to our page so we know it was successful.
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)