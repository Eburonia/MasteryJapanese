'''
    Question Generator
'''

import random

from verbs import verbs

# Import tenses
from tenses import present_polite_positive
from tenses import present_polite_negative
from tenses import past_polite_positive
from tenses import past_polite_negative

from tenses import present_plain_positive
from tenses import present_plain_negative
from tenses import past_plain_positive
from tenses import past_plain_negative

Verbs = list(verbs)


current_question = ''
current_answer = ''


def reset_verbs():

    ''' Reset the verbs '''

    global Verbs
    Verbs = list(verbs)


def generate_question():

    ''' Generate Question '''

    global current_answer

    if len(Verbs) > 0:

        # Get a random verb from the list
        random_verb = random.choice(list(Verbs))

        # Remove the verb from the list
        Verbs.remove(random_verb)

        # Get a random tense to fire a question
        random_tense = random.randint(1, 8)

        if random_tense == 1:
            current_answer = present_polite_positive(random_verb)
            return verbs[random_verb]['present_en'] + ' (polite)'

        if random_tense == 2:
            current_answer = present_polite_negative(random_verb)
            return f'not {verbs[random_verb]["present_en"]} (polite)'

        if random_tense == 3:
            current_answer = past_polite_positive(random_verb)
            return verbs[random_verb]['past_en'] + ' (polite)'

        if random_tense == 4:
            current_answer = past_polite_negative(random_verb)
            return f'not {verbs[random_verb]["past_en"]} (polite)'

        if random_tense == 5:
            current_answer = present_plain_positive(random_verb)
            return verbs[random_verb]['present_en'] + ' (plain)'

        if random_tense == 6:
            current_answer = present_plain_negative(random_verb)
            return f'not {verbs[random_verb]["present_en"]} (plain)'

        if random_tense == 7:
            current_answer = past_plain_positive(random_verb)
            return verbs[random_verb]['past_en'] + ' (plain)'

        if random_tense == 8:
            current_answer = past_plain_negative(random_verb)
            return f'not {verbs[random_verb]["past_en"]} (plain)'

    else:
        return 'end'


def check_question():

    ''' Check Question '''

    return current_answer


def show_answer():

    ''' Show Answer '''

    return current_answer
