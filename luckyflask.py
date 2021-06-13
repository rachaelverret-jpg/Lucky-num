from random import randint
import requests
from flask import Flask, request, jsonify, render_template
from forms import LuckyNumberRequestForm

app = Flask(__name__)


def get_fact_for_num(num, type="trivia"):
    """Given a number, get a fact about it from numberapi."""

    resp = requests.get(f"http://numbersapi.com/{num}/{type}")
    return resp.text


@app.route("/api/get-lucky-num", methods=["POST"])
def get_lucky_num():
    """Get lucky num, validating input & returning info about num."""

    received = request.json

    form = LuckyNumberRequestForm(csrf_enabled=False, data=received)

    if form.validate_on_submit():
        num = randint(1, 100)
        year = received['year']

        return jsonify(
            num={"num": num,
                 "fact": get_fact_for_num(num)},
            year={"year": year,
                  "fact": get_fact_for_num(year, type="year")},
        )

    else:
        return jsonify(errors=form.errors)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")