#!/usr/bin/env python3
"""module for flask app and initraing a babel"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """class for babels configs"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel(app)

app.config.from_object(Config)


@app.route("/")
def index():
    """rendering the templates"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
