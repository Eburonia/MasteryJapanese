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

VERBS = list(verbs)

CURRENT_ANSWER = ''


def reset_verbs():

    ''' Reset the verbs '''

    global VERBS

    VERBS = list(verbs)


def get_number_of_verbs():

    ''' Get the number of verbs '''

    global VERBS

    return len(VERBS)


def generate_question():

    ''' Generate Question '''

    global CURRENT_ANSWER

    if len(VERBS) > 0:

        # Get a random verb from the list
        random_verb = random.choice(list(VERBS))

        # Remove the verb from the list
        VERBS.remove(random_verb)

        # Get a random tense to fire a question
        random_tense = random.randint(1, 8)

        if random_tense == 1:
            CURRENT_ANSWER = present_polite_positive(random_verb)
            return verbs[random_verb]['present_en'] + ' (polite)'

        if random_tense == 2:
            CURRENT_ANSWER = present_polite_negative(random_verb)
            return f'not {verbs[random_verb]["present_en"]} (polite)'

        if random_tense == 3:
            CURRENT_ANSWER = past_polite_positive(random_verb)
            return verbs[random_verb]['past_en'] + ' (polite)'

        if random_tense == 4:
            CURRENT_ANSWER = past_polite_negative(random_verb)
            return f'not {verbs[random_verb]["past_en"]} (polite)'

        if random_tense == 5:
            CURRENT_ANSWER = present_plain_positive(random_verb)
            return verbs[random_verb]['present_en'] + ' (plain)'

        if random_tense == 6:
            CURRENT_ANSWER = present_plain_negative(random_verb)
            return f'not {verbs[random_verb]["present_en"]} (plain)'

        if random_tense == 7:
            CURRENT_ANSWER = past_plain_positive(random_verb)
            return verbs[random_verb]['past_en'] + ' (plain)'

        if random_tense == 8:
            CURRENT_ANSWER = past_plain_negative(random_verb)
            return f'not {verbs[random_verb]["past_en"]} (plain)'

    else:

        return 'end'


def check_question():

    ''' Check Question '''

    return CURRENT_ANSWER


def show_answer():

    ''' Show Answer '''

    return CURRENT_ANSWER
