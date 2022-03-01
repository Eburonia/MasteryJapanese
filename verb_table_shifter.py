'''
Verb Table Shifter
'''


def verb_table_shifter(verb, column):

    ''' Verb Table Shifter '''

    last_syllable = verb[-1:]

    if last_syllable == 'う':

        if column == 1:
            return 'わ'

        if column == 2:
            return 'い'

        if column == 4:
            return 'え'

        if column == 5:
            return 'お'

    elif last_syllable == 'く':

        if column == 1:
            return 'か'

        if column == 2:
            return 'き'

        if column == 4:
            return 'け'

        if column == 5:
            return 'こ'

    elif last_syllable == 'す':

        if column == 1:
            return 'さ'

        if column == 2:
            return 'し'

        if column == 4:
            return 'せ'

        if column == 5:
            return 'そ'

    elif last_syllable == 'つ':

        if column == 1:
            return 'た'

        if column == 2:
            return 'ち'

        if column == 4:
            return 'て'

        if column == 5:
            return 'と'

    elif last_syllable == 'ぬ':

        if column == 1:
            return 'な'

        if column == 2:
            return 'に'

        if column == 4:
            return 'ね'

        if column == 5:
            return 'の'

    elif last_syllable == 'む':

        if column == 1:
            return 'ま'

        if column == 2:
            return 'み'

        if column == 4:
            return 'め'

        if column == 5:
            return 'も'

    elif last_syllable == 'る':

        if column == 1:
            return 'ら'

        if column == 2:
            return 'り'

        if column == 4:
            return 'れ'

        if column == 5:
            return 'ろ'

    elif last_syllable == 'ぐ':

        if column == 1:
            return 'が'

        if column == 2:
            return 'ぎ'

        if column == 4:
            return 'げ'

        if column == 5:
            return 'ご'

    elif last_syllable == 'ぶ':

        if column == 1:
            return 'ば'

        if column == 2:
            return 'び'

        if column == 4:
            return 'べ'

        if column == 5:
            return 'ぼ'
