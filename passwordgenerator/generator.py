import random
import string

adjectives = [
    'sleepy', 'slow', 'smelly',
    'wet', 'fat', 'red',
    'orange', 'yellow', 'green',
    'blue', 'purple', 'fluffy',
    'white', 'proud', 'brave',
    'strong', 'weak', 'rainy'
]
nouns = [
    'apple', 'dinosaur', 'ball',
    'toaster', 'goat', 'dragon',
    'hammer', 'duck', 'panda',
    'lion', 'monkey', 'donkey'
]

def generate_password():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    return adjective + special_char + noun + str(number)
    