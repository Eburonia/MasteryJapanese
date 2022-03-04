import os
from question_generator import generate_question
from question_generator import reset_verbs
from question_generator import show_answer

from flask import (Flask, render_template, request, url_for, redirect)


if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/", methods=["GET", "POST"])
def index():

    ''' This is the index page '''

    # Set variables
    question = ''
    answer = ''
    message_color = ''
    given_answer = ''

    if request.method == 'POST':

        # Get the input answer from the end-user
        given_answer = request.form.get('answer')

        # Get the answer
        answer = show_answer()

        # Compare answer with given answer
        if answer == given_answer:

            # Don't show given answer
            given_answer = ''

            # Set correct color (green)
            message_color = 'limegreen'

        else:

            # Get the input answer from the end-user
            given_answer = request.form.get('answer')

            # Set wrong color (red)
            message_color = 'red'

        # Generate question
        question = generate_question()

    else:

        # Generate question
        question = generate_question()

    return render_template("index.html", question=question, answer=answer,
                            message_color=message_color, given_answer=given_answer)


@app.route("/reset_practice")
def reset_practice():

    ''' Reset the Verb set '''

    reset_verbs()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
