'''
    Tenses
'''

from verb_table_shifter import verb_table_shifter
from te_form_generator import te_form
from verbs import verbs


# Present Polite Positive
def present_polite_positive(verb):

    ''' Present Polite Positive '''

    # Get the verb type (ru/u)
    verb_type = verbs[verb]['type']

    # When 'ru' verb
    if verb_type == 'ru':
        return verb[:-1] + 'ます'

    # When 'u' verb
    elif verb_type == 'u':
        return verb[:-1] + verb_table_shifter(verb, 2) + 'ます'

    # When not 'ru' or 'u' verb
    else:
        return 'error'


# Present Polite Negative
def present_polite_negative(verb):

    ''' Present Polite Negative '''

    # Get the verb type (ru/u)
    verb_type = verbs[verb]['type']

    # When 'ru' verb
    if verb_type == 'ru':
        return verb[:-1] + 'ません'

    # When 'u' verb
    elif verb_type == 'u':
        return verb[:-1] + verb_table_shifter(verb, 2) + 'ません'

    # When not 'ru' or 'u' verb
    else:
        return 'error'


# Past Polite Positive
def past_polite_positive(verb):

    ''' Past Polite Positive '''

    # Get the verb type (ru/u)
    verb_type = verbs[verb]['type']

    # When 'ru' verb
    if verb_type == 'ru':
        return verb[:-1] + 'ました'

    # When 'u' verb
    elif verb_type == 'u':
        return verb[:-1] + verb_table_shifter(verb, 2) + 'ました'

    # When not 'ru' or 'u' verb
    else:
        return 'error'


# Past Polite Negative
def past_polite_negative(verb):

    ''' Past Polite Negative '''

    # Get the verb type (ru/u)
    verb_type = verbs[verb]['type']

    # When 'ru' verb
    if verb_type == 'ru':
        return verb[:-1] + 'ませんでした'

    # When 'u' verb
    elif verb_type == 'u':
        return verb[:-1] + verb_table_shifter(verb, 2) + 'ませんでした'

    # When not 'ru' or 'u' verb
    else:
        return 'error'


# Present Plain Positive
def present_plain_positive(verb):

    ''' Present Plain Positive '''

    return verb


# Present Plain Negative
def present_plain_negative(verb):

    ''' Present Plain Negative '''

    # Get the verb type (ru/u)
    verb_type = verbs[verb]['type']

    # When 'ru' verb
    if verb_type == 'ru':
        return verb[:-1] + 'ない'

    # When 'u' verb
    elif verb_type == 'u':
        return verb[:-1] + verb_table_shifter(verb, 1) + 'ない'

    # When not 'ru' or 'u' verb
    else:
        return 'error'


# Past Plain Positive
def past_plain_positive(verb):

    ''' Past Plain Positive '''

    # Get the verb type (ru/u)
    verb_type = verbs[verb]['type']

    # When 'ru' verb
    if verb_type == 'ru':

        return te_form(verb)[:-1] + 'た'

    # When 'u' verb
    elif verb_type == 'u':

        if te_form(verb)[-1:] == 'て':
            return te_form(verb)[:-1] + 'た'

        elif te_form(verb)[-1:] == 'で':
            return te_form(verb)[:-1] + 'だ'

        else:
            return 'error'

    else:
        return 'error'


# Past Plain Negative
def past_plain_negative(verb):

    ''' Past Plain Negative '''

    # Get the verb type (ru/u)
    verb_type = verbs[verb]['type']

    # When 'ru' verb
    if verb_type == 'ru':
        return verb[:-1] + 'なかった'

    # When 'u' verb
    elif verb_type == 'u':
        return verb[:-1] + verb_table_shifter(verb, 1) + 'なかった'

    # When not 'ru' or 'u' verb
    else:
        return 'error'
