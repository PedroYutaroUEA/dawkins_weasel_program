import random
import re

POSSIBLE_CHARS = 'abcdefghijklmnopqrstuvwxyz1234567890 '  # DEFINES LETTERS TO BE EXCHANGED
still_playing = 'y'
target_phrase = ''
generation = 0
score = 0
best_score = 0
candidate = ""
accuracy = 0


# REGEX AND SIZE VERIFICATION
def validation(target, phrase_ref):
    reg_violation = bool(re.search(r'[^a-z0-9\s]', target) or re.search(r'[^a-z0-9\s]', phrase_ref))
    diff_size = bool(len(target) != len(phrase_ref))
    return reg_violation or diff_size


# THIS CREATE 100 COPIES OF THE PHRASE_REF
def reproduction(phrase_ref):
    if len(phrase_ref) > 0:
        hundred_phrase = [list(phrase_ref) for _ in range(100)]
        mutation(hundred_phrase)
    else:
        mutation([list(phrase) for _ in range(100)])


# MUTATES THE PHRASE
def mutation(sentence):
    p = 0
    for phrases in sentence:
        c = 0
        for _ in phrases:
            word_rand = random.choice(POSSIBLE_CHARS)
            if random.randint(1, 100) <= 5:  # Has a 5% to mutate a letter
                sentence[p][c] = word_rand
            c += 1
        p += 1
    selection(sentence)


# SELECTS THE PHRASE USED FOR THE NEXT GENERATION
def selection(candidates):
    global score, best_score, generation, candidate, accuracy
    for phrases in candidates:
        score = position = 0  # Resets to 0
        for char in phrases:  # Compares if the phrases have the same char at the same position of "target_phrase"
            if char == target_phrase[position]:
                score += 1
            position += 1
        if score > best_score:  # Used to select the best candidate
            best_score = score
            candidate = ''.join(phrases)
            accuracy = (score / len(target_phrase)) * 100
    if len(candidate) > 0:
        print(f"Generation {str(generation)}: {candidate} - Score {str(best_score)} | Accuracy: {accuracy:.2f}%")
    if best_score == len(target_phrase):
        print("========== SIMULATION ENDED! ==========")
        print(f"Best generation: Nº{generation}")
    else:
        if len(candidate) > 0:
            generation += 1
        reproduction(candidate)


# THIS START THE 'INPUT PHASE'
while still_playing == 'y':
    target_phrase = str(input("Set the target phrase: ")).lower()
    phrase = str(input(f"Set a phrase with {len(target_phrase)} chars (space is included as a char): ")).lower()

    # THIS RESTART DE INPUT IF THE USER DONT COMPLY WITH THE REGEX REQUIREMENT
    while validation(target_phrase, phrase):
        print(f"Both phrases must match [a-z0-9] regex and length (target: {target_phrase}, phrase: {phrase})")
        target_phrase = str(input("Set the target phrase: ")).lower()
        phrase = str(input(f"Set a phrase with {len(target_phrase)} chars (space is included as a char): ")).lower()
        validation(target_phrase, phrase)

    # THIS CHECK IF THE USER INPUT IS EQUAL TO THE KEY-PHRASE
    if phrase == target_phrase and generation == 0:
        print(f'The phrase you typed is exactly what this program should try ({phrase})! :O')

    # THIS PRINT 100 COPIES OF USER'S INPUT
    else:
        reproduction(phrase)
        generation = score = best_score = 0  # Resets everything to 0
        candidate = ''

    # ASK IF THE USER WANTS TO PLAY AGAIN
    still_playing = str(input('Wanna play again (Y/N)?: ')).lower()
    while still_playing not in ('Y', 'y', 'N', 'n'):
        print(f"Invalid response (you typed '{still_playing}')")
        still_playing = str(input('Wanna play again (Y/N)?: ')).lower()

print('Thanks for playing! :)')
