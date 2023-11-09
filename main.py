import re

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

    if phrase == target_phrase and generation == 0:
        print(f'The phrase you typed is exactly what this program should try ({phrase})! :O')
    else:
        print(reproduction(phrase))

    still_playing = str(input('Wanna play again (Y/N)?: ')).lower()
    while still_playing not in ('Y', 'y', 'N', 'n'):
        print(f"Invalid response (you typed '{still_playing}')")
        still_playing = str(input('Wanna play again (Y/N)?: ')).lower()

print('Thanks for playing! :)')
