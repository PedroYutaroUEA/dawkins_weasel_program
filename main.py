import random
import string


def print_hi(user_name):
    print(f'Hi, {user_name}')


if __name__ == '__main__':
    print_hi('PyCharm')

name = 'pedro'
age = 18

if age >= 18:
    print(f'{name} é maior de idade')
else:
    print(f'{name} é menor de idade')


def reproduction(phrase):
    words = list(phrase)
    words_cp100 = [words for i in range(100)]
    return words_cp100

def mutation(rep_result):
    for result in rep_result:
        for char in result:
            probability = random.random()
            condition = probability == 1
            char = random.choice(string.ascii_lowercase) if condition else char

phrase = str(input("Set a phrase with 10 char: ")).lower()
while len(phrase) != 10:
    phrase = str(input("Please, set a phrase with 10 char: ")).lower()

rep_result = reproduction(phrase)
print(mutation(rep_result))