''' Te Form Generator '''


from verbs import verbs


def te_form(verb, ret):

    ''' Te form generator
    ret = 0 = return Hiragana or Mazegaki
    ret = 1 = return Mazegaki '''

    # Get the verb type (ru/u)
    type_ = verbs[verb]['type']

    # When 'ru' verb
    if type_ == 'ru':

        if ret == 0:

            # Return Hiragana
            return verb[:-1] + 'て'

        if ret == 1:

            # Return Mazegaki
            return verbs[verb]['hiragana'][:-1] + 'て'

        else:

            return 'ERROR 1'

    # When 'u' verb
    elif type_ == 'u':

        last_syllable = verb[-1:]

        if last_syllable == 'う':

            # Return Hiragana
            if ret == 0:

                return verb[:-1] + 'って'

            # Return Mazegaki
            if ret == 1:

                return verbs[verb]['hiragana'][:-1] + 'って'

            else:

                return 'ERROR 2'

        elif last_syllable == 'く':

            return verb[:-1] + 'いて'

        elif last_syllable == 'す':

            return verb[:-1] + 'して'

        elif last_syllable == 'つ':

            return verb[:-1] + 'って'

        elif last_syllable == 'ぬ':

            return verb[:-1] + 'んで'

        elif last_syllable == 'む':

            # Return Hiragana
            if ret == 0:

                return verb[:-1] + 'んで'

            # Return Mazegaki
            if ret == 1:

                return verbs[verb]['hiragana'][:-1] + 'んで'

            else:

                return 'ERROR 3'

        elif last_syllable == 'る':

            return verb[:-1] + 'って'

        elif last_syllable == 'ぐ':

            return verb[:-1] + 'いで'

        elif last_syllable == 'ぶ':

            return verb[:-1] + 'んで'

        else:

            return 'ERROR 4'

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 5'
