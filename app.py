import os

from flask import (Flask, flash, render_template, redirect, request,  url_for)


if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    ''' This is the index page '''

    test = ''

    if request.method == 'POST':

        test = 'hallo'

    return render_template("index.html", test=test)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
