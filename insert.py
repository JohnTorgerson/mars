# Import dependent libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

## set primary landing page application
@app.route("/")
def index():
    # find one document from our mongo db and return it.
    collection = mongo.db.collection.find_one()
    # pass that listing to render_template
    return render_template("index.html", collection=collection)

# set our path to /scrape
@app.route("/scrape")
def scrape():

    # call the scrape function in our scrape_mars file. This will scrape and save to mongo.
    collection_items = scrape_mars.scrape()

    # update our listings with the data that is being scraped.
    mongo.db.collection.update_one({}, {"$set": collection_items}, upsert=True)

    # print confirmation
    print("Newly Scraped Data Uploaded!") 

    # return a message to our page so we know it was successful.
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)