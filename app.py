''' App.py '''

import os
import random

from flask import (Flask, render_template, request, url_for, redirect, session)
from verbs import verbs
from tenses import present_polite_positive
from tenses import present_polite_negative


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
    color = None
    disable_input = ''

    # Assign stats
    correct_answers_stat = 5
    incorrect_answers_stat = 8

    # POST request
    if request.method == 'POST':

        # When verbs are in session_memory cookie
        if len(session['session_memory']) > 0:

            # Check given answer with correct answer
            correct_answer = check_answer(request.form.get('answer'), session['answers'])

            # Set correct answer
            answer = correct_answer['correct_answer']

            # Set green or red color (correct or incorrect answer)
            color = correct_answer['answer_color']

            # Generate a new question
            question_and_answer = generate_question_answer()

            # Send question to front-end
            question = question_and_answer['question']

            # Save the answers in a cookie
            session['answers'] = {
                'answer_hiragana': question_and_answer['answer_hiragana'],
                'answer_mazegaki': question_and_answer['answer_mazegaki']
            }

        # When no more verbs in session_memory cookie
        else:

            # Send question to front-end
            question = 'END SESSION'

            # Check given answer with correct answer
            correct_answer = check_answer(request.form.get('answer'), session['answers'])

            # Set correct answer
            answer = correct_answer['correct_answer']

            # Set green or red color (correct or incorrect answer)
            color = correct_answer['answer_color']

            # Disable the input textbox
            disable_input = 'disabled'

    # GET request
    else:

        # Start of practice session

        # Load the verbs in the session_memory cookie
        session['session_memory'] = list(verbs)

        # Generate a new question
        question_and_answer = generate_question_answer()

        # Send question to front-end
        question = question_and_answer['question']

        # Save the answers in a cookie
        session['answers'] = {
            'answer_hiragana': question_and_answer['answer_hiragana'],
            'answer_mazegaki': question_and_answer['answer_mazegaki']
            }

        # Show no answer when first question is fired
        answer = ''

    # Render the practice page
    return render_template("index.html",
                           question=question, answer=answer,
                           color=color, disable_input=disable_input,
                           correct_answers_stat=correct_answers_stat,
                           incorrect_answers_stat=incorrect_answers_stat)


def check_answer(given_answer, correct_answers):

    ''' Check Answer '''

    # Correct Hiragana answer
    if given_answer == correct_answers['answer_hiragana']:

        # Return correct Hiragana answer + green color
        ret = {
            'correct_answer': correct_answers['answer_hiragana'],
            'answer_color': 'limegreen'
            }

        return ret

    # Correct Mazegaki answer
    elif given_answer == correct_answers['answer_mazegaki']:

        # Return correct Mazegaki answer + green color
        ret = {
            'correct_answer': correct_answers['answer_mazegaki'],
            'answer_color': 'limegreen'
            }

        return ret

    # Incorrect answer
    else:

        # Return correct Mazegaki answer + red color
        ret = {
            'correct_answer': correct_answers['answer_mazegaki'],
            'answer_color': 'red'
            }

        return ret


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


def assign_random_tense(verb):

    ''' Generate a random tense '''

    tense_number = random.randint(1, 2)

    if tense_number == 1:

        return present_polite_positive(verb)

    if tense_number == 2:

        return present_polite_negative(verb)


def generate_question_answer():

    ''' Generate Question '''

    # Get a verb from the session_memory
    verb = get_verb_from_session(session['session_memory'])

    # Assign a random tense to the verb
    question_and_answer = assign_random_tense(verb)

    # Set the question and answers
    question = question_and_answer[0]
    answer_hiragana = question_and_answer[1]
    answer_mazegaki = question_and_answer[2]

    # Combine the question and answers
    question_and_answer = {
        'question': question,
        'answer_hiragana': answer_hiragana,
        'answer_mazegaki': answer_mazegaki
        }

    # Return the question and answers
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
