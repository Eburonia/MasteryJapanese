''' App.py '''

import os
from flask import (Flask, render_template, request, url_for, redirect)

from question_generator import generate_question
from question_generator import reset_verbs
from question_generator import show_answer
from question_generator import get_number_of_verbs

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


correct_answers = 0
false_answers = 0

# Set the total number of verbs
total_questions = get_number_of_verbs()

@app.route("/", methods=["GET", "POST"])
def index():

    ''' This is the index page '''

    # Set variables
    question = ''
    answer = ''
    message_color = ''
    given_answer = ''

    global correct_answers
    global false_answers
    global total_questions

    # POST request
    if request.method == 'POST':

        # Get the input answer from the end-user
        given_answer = request.form.get('answer')

        # Get the answer
        answer = show_answer()

        if(false_answers + correct_answers < total_questions):

            # When answer with given answer are equal (correct answer)
            if answer[0] == given_answer or answer[1] == given_answer:

                # Check Hiragana answer
                if answer[0] == given_answer:

                    # Show Hiragana
                    answer = answer[0]

                    # Increment correct answers
                    correct_answers = correct_answers + 1

                # Check Mazegaki answer
                elif answer[1] == given_answer:

                    # Show Mazegaki answer
                    answer = answer[1]

                    # Increment correct answers
                    correct_answers = correct_answers + 1

                else:

                    # Show error
                    answer = 'ERROR30'

                # Don't show given answer
                given_answer = ''

                # Set correct color (green)
                message_color = 'limegreen'

            # When answer with given answer are not equal (incorrect answer)
            else:

                # Get the input answer from the end-user
                given_answer = request.form.get('answer')

                # Set wrong color (red)
                message_color = 'red'

                # Show Hiragana and Mazegaki answer
                answer = f'{answer[1]}【{answer[0]}】'

                # Increment false answers
                false_answers = false_answers + 1

        if get_number_of_verbs() != 0:

            # Generate new question
            question = generate_question()

    # GET request
    else:

        if get_number_of_verbs() != 0:

            # Generate question
            question = generate_question()

    # Render the page
    return render_template(
        "index.html", question=question, answer=answer,
        message_color=message_color, given_answer=given_answer,
        correct_answers=correct_answers, false_answers=false_answers,
        total_questions=total_questions)


@app.route("/reset_practice")
def reset_practice():

    ''' Reset the Verb set '''

    global correct_answers
    global false_answers
    global total_questions

    correct_answers = 0
    false_answers = 0

    reset_verbs()

    total_questions = get_number_of_verbs()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
