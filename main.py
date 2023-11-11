import random
import re

letters = 'abcdefghijklmnopqrstuvwxyz1234567890 '  # DEFINES LETTERS TO BE EXCHANGED
still_playing = 'y'
target_phrase = ''
generation = 0
score = 0
best_score = 0
candidate = ""


# THIS CREATE 100 COPIES OF THE PHRASE_REF
def reproduction(phrase_ref):
    hundred_phrase = [list(phrase_ref) for _ in range(100)]
    mutation(hundred_phrase)


# MUTATES THE PHRASE
def mutation(sentence):
    global target_phrase
    x = 0
    for phrases in sentence:
        y = 0
        for _ in phrases:
            word_rand = random.choice(letters)
            if random.randint(1, 100) <= 5:  # Has a 5% to mutate a letter
                sentence[x][y] = word_rand
            y += 1
        x += 1

    selection(sentence)


# Can't use "phrases" nor "_" to manipulate "sentence" in line 27, since they are not int type variables
# Use "print(type(nameOfVariable))" to identify the type of variable


# SELECTS THE PHRASE USED FOR THE NEXT GENERATION
def selection(candidates):
    global score
    global best_score
    global generation
    global candidate
    for phrases in candidates:
        score = position = 0  # Resets to 0
        for char in phrases:  # Compares if the phrases have the same char at the same position of "target_phrase"
            if char == target_phrase[position]:
                score += 1
            position += 1
        if score > best_score:  # Used to select the best candidate
            best_score = score
            candidate = ''.join(phrases)
    print("Generation " + str(generation) + ": " + candidate + " - Score " + str(best_score))
    if best_score == len(target_phrase):
        print("========== SIMULATION ENDED! ==========")
        print(f"Best generation: Nº{generation}")
    else:
        generation += 1
        reproduction(candidate)


# THIS START THE 'INPUT PHASE'
while still_playing == 'y':
    target_phrase = str(input("Set the target phrase: ")).lower()
    phrase = str(input(f"Set a phrase with {len(target_phrase)} chars (space is included as a char): ")).lower()
    is_target_invalid = bool(re.search(r'[^a-z0-9\s]', target_phrase))
    is_phrase_invalid = bool(re.search(r'[^a-z0-9\s]', phrase))

    # THIS RESTART DE INPUT IF THE USER DONT COMPLY WITH THE REGEX REQUIREMENT
    while is_target_invalid or is_phrase_invalid or len(phrase) != len(target_phrase):
        print(f"Both phrases must match [a-z0-9] regex and length (target: {target_phrase}, phrase: {phrase})")
        target_phrase = str(input("Set the target phrase: ")).lower()
        phrase = str(input(f"Set a phrase with {len(target_phrase)} chars (space is included as a char): ")).lower()
        is_target_invalid = bool(re.search(r'[^a-z0-9\s]', target_phrase))
        is_phrase_invalid = bool(re.search(r'[^a-z0-9\s]', phrase))

    # THIS CHECK IF THE USER INPUT IS EQUAL TO THE KEY-PHRASE
    if phrase == target_phrase and generation == 0:
        print(f'The phrase you typed is exactly what this program should try ({phrase})! :O')

    # THIS PRINT 100 COPIES OF USER'S INPUT
    else:
        generation = score = best_score = 0  # Resets everything to 0
        candidate = ""
        reproduction(phrase)

    # ASK IF THE USER WANTS TO PLAY AGAIN
    still_playing = str(input('Wanna play again (Y/N)?: ')).lower()
    while still_playing not in ('Y', 'y', 'N', 'n'):
        print(f"Invalid response (you typed '{still_playing}')")
        still_playing = str(input('Wanna play again (Y/N)?: ')).lower()

print('Thanks for playing! :)')
