import random
from characters import letters, numbers, symbols

print("Welcome to the Python Password Generator!")
no_of_characters = int(input("How many characters would you like?\n"))

print('Password - ',''.join(random.sample(letters+numbers+symbols, no_of_characters)))