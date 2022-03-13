'''
    Question Generator
'''

import random

from verbs import verbs

# Import tenses
#from tenses import present_polite_positive
#from tenses import present_polite_negative
#from tenses import past_polite_positive
#from tenses import past_polite_negative

#from tenses import present_plain_positive
#from tenses import present_plain_negative
#from tenses import past_plain_positive
#from tenses import past_plain_negative


VERBS = list(verbs)


def get_random_verb_from_list():

    ''' Get a random verb from the list '''

    if len(VERBS) > 0:

        # Get a random verb from the list
        random_verb = random.choice(list(VERBS))

        VERBS.remove(random_verb)

        return random_verb

    else:

        return 'end of practice session'


def check_answer(given_question, given_answer):

    ''' Check the answer '''

    if given_question == given_answer:

        return 'correct'

    else:

        return 'incorrect'


def generate_question():

    ''' Generate a question '''

    random_verb = get_random_verb_from_list()

    question = random_verb
    answer = random_verb

    question_and_answer = {'question': question, 'answer': answer}

    print(question_and_answer)

    return question_and_answer


def reset_verbs():

    ''' Reset the verbs '''

    global VERBS

    VERBS = list(verbs)