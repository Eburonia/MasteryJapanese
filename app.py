''' App.py '''

import os
import random

from flask import (Flask, render_template, request, url_for, redirect, session)
from verbs import verbs
from tenses import present_polite_positive


if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/", methods=["GET", "POST"])
def index():

    ''' This is the index page '''

    # Assign question and answer
    question = None
    answer = None

    # POST request
    if request.method == 'POST':

        # When verbs are in session_memory cookie
        if len(session['session_memory']) > 0:

            # Check given answer with correct answer
            answer = check_answer(request.form.get('answer'), session['answer'])

            # Generate a new question
            question_and_answer = generate_question_answer()

            # Send question to front-end
            question = question_and_answer['question']

            # Save the answer in a cookie
            session['answer'] = question_and_answer['answer']

        # When no more verbs in session_memory cookie
        else:

            # Send question to front-end
            question = 'END'

            # Check given answer with correct answer
            answer = check_answer(request.form.get('answer'), session['answer'])

    # GET request
    else:

        # Load the verbs in the session_memory cookie
        session['session_memory'] = list(verbs)

        # Generate a new question
        question_and_answer = generate_question_answer()

        # Send question to front-end
        question = question_and_answer['question']

        # Save the answer in a cookie
        session['answer'] = question_and_answer['answer']

        # Show no answer when first question is fired
        answer = ''

    # Render the practice page
    return render_template("index.html",
                           question=question, answer=answer)


def check_answer(given_answer, correct_answer):

    ''' Check Answer '''

    # Correct answer
    if given_answer == correct_answer:

        return 'correct answer'

    # Incorrect answer
    else:

        return 'incorrect answer'


def get_verb_from_session(session_memory):

    '''
    Return a verb from the session_memory and remove
    it from the memory_session
    '''

    # Get the session_memory from cookie
    session_memory = session['session_memory']

    # If there is verbs in session
    if len(session_memory) > 0:

        # Get a random verb from the session_memory
        random_verb = random.choice(list(session_memory))

        # Remove this verb from the session_memory
        session_memory.remove(random_verb)

        # Update the session_memory coookie
        session['session_memory'] = session_memory

        # Return the verb
        return random_verb

    # When no more verbs in session
    else:

        # Return message
        return 'end'


def generate_question_answer():

    ''' Generate Question '''

    # Get a verb from the session_memory
    verb = get_verb_from_session(session['session_memory'])

    # Generate a random tense here !!!!
    # generate_random_tense(verb, tenses)

    # Get the question and answer
    question_and_answer = present_polite_positive(verb)

    # Set the question and answer
    question = question_and_answer[0]
    answer = question_and_answer[1]

    # Combine the question and answer
    question_and_answer = {'question': question, 'answer': answer}

    # Return the question and answer
    return question_and_answer


@app.route("/reset_session_memory")
def reset_session_memory():

    ''' Reset session memory '''

    # Reset the session_memory
    session['session_memory'] = list(verbs)

    # Return to index page
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
