import random
import re

letters = 'abcdefghijklmnopqrstuvwxyz '  # DEFINES LETTERS TO BE EXCHANGED
still_playing = 'y'
target_phrase = 'methinks it is like a weasel'
generation = 0
score = 0
phrase_score = {}


# THIS CREATE 100 COPIES OF THE PHRASE_REF


def reproduction(phrase_ref):
    hundred_phrase = [list(phrase_ref) for _ in range(100)]
    return hundred_phrase

# MUTATES THE PHRASE


def mutation(sentence):
    global target_phrase  # GLOBAL IS USED TO TURN THE VARIABLES USABLE IN ALL CODE
    global score
    global generation
    global phrase_score
    for child in range(100):
        score = 0
        for char in range(28):
            word_rand = random.choice(letters)
            # first char
            if char == 0:
                sentence = str(word_rand + sentence[1:])
            if 1 <= char < 28:
                sentence = str(sentence[0:char] + word_rand + sentence[char + 1:])
            # last char
            else:
                sentence = str(sentence[0:char] + word_rand)
            generation += 1
            if word_rand == target_phrase[char]:
                score += 1
        allocator = sentence
        phrase_score[allocator] = score, generation
        return sentence


# THIS START DE 'INPUT PHASE'

while still_playing == 'y':
    phrase = str(input("Set a phrase with 28 chars (space is included as a char): ")).lower()
    is_invalid = bool(re.search(r'[^a-z\s]', phrase))

    # THIS RESTART DE INPUT IF THE USER DONT COMPLY WITH THE REQUIREMENT

still_playing = 'y'
target_phrase = 'methinks it is like a weasel'
generation = 0


def reproduction(phrase_ref):
    hundred_phrase = [list(phrase_ref) for _ in range(100)]
    return hundred_phrase


while still_playing == 'y':
    phrase = str(input("Set a phrase with 28 chars (space is included as a char): ")).lower()
    is_invalid = bool(re.search(r'[^a-z\s]', phrase))

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

    if phrase == target_phrase and generation == 0:
        print(f'The phrase you typed is exactly what this program should try ({phrase})! :O')
    else:
        print(reproduction(phrase))


    still_playing = str(input('Wanna play again (Y/N)?: ')).lower()
    while still_playing not in ('Y', 'y', 'N', 'n'):
        print(f"Invalid response (you typed '{still_playing}')")
        still_playing = str(input('Wanna play again (Y/N)?: ')).lower()

print('Thanks for playing! :)')
