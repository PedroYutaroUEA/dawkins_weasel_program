import random
import re

letters = 'abcdefghijklmnopqrstuvwxyz '  # DEFINES LETTERS TO BE EXCHANGED
still_playing = 'y'
target_phrase = 'methinks it is like a weasel'
generation = 0
pontuation = 0
phrase_pontuation = {}

# THIS CREATE 100 COPIES OF THE PHRASE_REF


def reproduction(phrase_ref):
    hundred_phrase = [list(phrase_ref) for _ in range(100)]
    return hundred_phrase

# MUTATES THE PHRASE


def mutation(sentence):
    global target_phrase  # GLOBAL IS USED TO TURN THE VARIABLES USABLE IN ALL CODE
    global pontuation
    global generation
    global phrase_pontuation
    for c in range(100):
        pontuation = 0
        for w in range(28):
            word_rand = random.choice(letters)
            if w == 0:
                sentence = word_rand + sentence[1:]
            if 1 < w < 28:
                sentence = sentence[0:w] + word_rand + sentence[w + 1:]
            else:
                sentence = sentence[0:w] + word_rand
            generation += 1
            if word_rand == target_phrase[w]:
                pontuation += 1
        alocator = sentence
        phrase_pontuation[alocator] = pontuation
        return sentence


# THIS START DE 'INPUT PHASE'


while still_playing == 'y':
    phrase = str(input("Set a phrase with 28 chars (space is included as a char): ")).lower()
    is_invalid = bool(re.search(r'[^a-z\s]', phrase))

    # THIS RESTART DE INPUT IF THE USER DONT COMPLY WITH THE REQUIREMENT

    while len(phrase) != 28 or is_invalid:
        phrase = str(input(f"The phrase must contains 28 letter chars (you typed {phrase}): ")).lower()
        is_invalid = bool(re.search(r'[^a-z\s]', phrase))

    # THIS CHECK IF THE USER INPUT IS EQUAL TO THE KEY-PHRASE

    if phrase == target_phrase and generation == 0:
        print(f'The phrase you typed is exactly what this program should try ({phrase})! :O')

    # THIS PRINT 100 COPIES OF USER'S INPUT

    else:
        print(reproduction(phrase))

    # ASK IF THE USER WANTS TO PLAY AGAIN

    still_playing = str(input('Wanna play again (Y/N)?: ')).lower()
    while still_playing not in ('Y', 'y', 'N', 'n'):
        print(f"Invalid response (you typed '{still_playing}')")
        still_playing = str(input('Wanna play again (Y/N)?: ')).lower()


print('Thanks for playing! :)')
