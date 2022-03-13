''' App.py '''

import os
from flask import (Flask, render_template, request, url_for, redirect)

from question_generator import generate_question
from question_generator import check_answer
from question_generator import reset_verbs


if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/", methods=["GET", "POST"])
def index():

    ''' This is the index page '''

    question = None
    answer = None

    # Get the given question from the question division
    given_question = request.form.get('question')

    # Get the given answer from the textfield
    given_answer = request.form.get('answer')

    # POST request
    if request.method == 'POST':

        # 
        correct_answers = int(request.form.get('correct_answers'))
        correct_answers = correct_answers + 1

        # Check the answer
        answer = check_answer(given_question, given_answer)

        # Generate new question
        question = generate_question()
        question = question['question']

    # GET request
    else:

        # Set the correct answers to 0
        correct_answers = 0

        # Generate new question
        question = generate_question()
        question = question['question']

    # Render the page
    return render_template("index.html", question=question, answer=answer,
                           correct_answers=correct_answers)


@app.route("/reset_practice")
def reset_practice():

    ''' Reset the Verb set '''

    reset_verbs()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
