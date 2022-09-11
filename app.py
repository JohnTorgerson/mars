# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    # movie_list = ["Attack of the Clones", "Revenge of the Sith", "Rogue One"]
    # return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)