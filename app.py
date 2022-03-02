import os
from question_generator import generate_question
from question_generator import check_question
from question_generator import show_answer

from flask import (Flask, render_template, request, url_for)


if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():

    ''' This is the index page '''

    question = ''
    answer = ''
    message_color = ''
    given_answer = ''

    if request.method == 'POST':

        # Get the answer
        answer = show_answer()

        # Get the input answer from the end-user
        given_answer = request.form.get('answer')

        # Compare answer with given answer
        if answer == given_answer:
            message_color = 'green'

        else:
            message_color = 'red'

        question = generate_question()

    else:
        question = generate_question()

    return render_template("index.html", question=question, answer=answer, message_color=message_color, given_answer=given_answer)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
