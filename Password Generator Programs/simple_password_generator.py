import random
from characters import letters, numbers, symbols

print("Welcome to the Python Password Generator!")
no_of_characters = int(input("How many characters would you like?\n"))


### Taking a random sample from the list of characters, the sample size is same as the number of characters
### as mentioned in the parameters. Using the join method to make a string out of this list. 

print('Password - ',''.join(random.sample(letters+numbers+symbols, no_of_characters)))