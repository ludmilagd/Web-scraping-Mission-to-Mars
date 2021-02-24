from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# mars_db.mars.drop()

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    Mars_info = mongo.db.Mars_collection.find_one()

    # Return template and data
    return render_template("index.html", Mars=Mars_info)


# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():

    
    # Run the scrape function
    Mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.Mars_collection.update({}, Mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
