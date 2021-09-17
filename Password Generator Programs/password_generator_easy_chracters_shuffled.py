import random
from characters import letters, numbers, symbols
password=[]

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for i in range(1, nr_letters+1):
  password.append( letters[random.randint(0,51)])

for i in range(1, nr_symbols+1):
  password.append(symbols[random.randint(0,8)])

for i in range(1, nr_numbers+1):
  password.append(str(numbers[random.randint(0,9)]))

random.shuffle(password)

print(f"Password Hard - {''.join(password)}")