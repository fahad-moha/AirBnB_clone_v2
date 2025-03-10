#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
app = Flask("___name____")

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """Return a given string"""
    return render_template("10-hbnb_filters.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
