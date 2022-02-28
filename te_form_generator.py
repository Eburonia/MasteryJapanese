'''
Te-form generator
'''


from verbs import verbs


def te_form(verb):

    ''' Te form generator '''

    # Get the verb type (ru/u)
    verb_type = verbs[verb]['type']

    # When 'ru' verb
    if verb_type == 'ru':
        return verb[:-1] + 'て'

    # When 'u' verb
    elif verb_type == 'u':

        last_syllable = verb[-1:]

        if last_syllable == 'う':
            return verb[:-1] + 'って'

        elif last_syllable == 'く':
            return verb[:-1] + 'いて'

        elif last_syllable == 'す':
            return verb[:-1] + 'して'

        elif last_syllable == 'つ':
            return verb[:-1] + 'って'

        elif last_syllable == 'ぬ':
            return verb[:-1] + 'んで'

        elif last_syllable == 'む':
            return verb[:-1] + 'んで'

        elif last_syllable == 'る':
            return verb[:-1] + 'って'

        elif last_syllable == 'ぐ':
            return verb[:-1] + 'いで'

        elif last_syllable == 'ぶ':
            return verb[:-1] + 'んで'

        else:
            return 'error'

    # When not 'ru' or 'u' verb
    else:
        return 'error'
