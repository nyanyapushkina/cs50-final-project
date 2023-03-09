import os
import re
import numpy as np

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():

    return render_template("index.html")

# Divide the poem into 4 peices. Display an apology, if the poem is too short. Create a page with cards, if poem is fine
@app.route("/learn", methods=["GET", "POST"])
def learn():
    """Enter the poem and split to learn"""
    if request.method == "POST":
        poem = request.form.get("poem")

        lines = 0

        for i in poem:
            if i == '\n':
                lines += 1
            lines += 1

        cards = lines / 2

        lines = 0
        for i in poem:
            if i == '\n':
                lines += 1

        poem_splitted = poem.split("\n")
        poem_splitted[:] = [value for value in poem_splitted if len(value) >= 2]

        poem_on_cards = np.array_split(poem_splitted, 4)

        quatrain_1 = '\n'.join(map(str, poem_on_cards[0]))
        quatrain_2 = '\n'.join(map(str, poem_on_cards[1]))
        quatrain_3 = '\n'.join(map(str, poem_on_cards[2]))
        quatrain_4 = '\n'.join(map(str, poem_on_cards[3]))

        if not request.form.get("poem"):
            return apology("Type in the poem")

        if len(poem)<4:
            return apology("There should be at least 2 quatrains")

        return render_template("poetry.html", quatrain_1 = quatrain_1, quatrain_2 = quatrain_2, quatrain_3 = quatrain_3, quatrain_4 = quatrain_4)

    else:
        return render_template("intex.html")

# Display a page with instructions
@app.route("/howto")
def howto():
     return render_template("howto.html")

# Display a page with info about the project and its creator
@app.route("/about")
def about():
     return render_template("about.html")