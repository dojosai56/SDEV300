"""Welcome to Python Flask Lab"""
from datetime import datetime
from flask import Flask, render_template
from flask import current_app as app


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    '''Method for Home Tab'''
    current_time = "Time Stamp: " + str(datetime.now())
    return render_template("index.html", timestamp=current_time)


@app.route("/about")
def about():
    '''Method for About Tab'''
    current_time = "Time Stamp: " + str(datetime.now())
    return render_template("about.html", timestamp=current_time)


@app.route("/photo_gallery")
def photo_gallery():
    '''Method for Photo Gallery Tab'''
    current_time = "Time Stamp: " + str(datetime.now())
    return render_template("photo_gallery.html", timestamp=current_time)


if __name__ == "__main__":
    app.run()
