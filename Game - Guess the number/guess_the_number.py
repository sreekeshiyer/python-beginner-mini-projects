#Number Guessing Game
import random
from art import logo

print(logo)
difficulty = (input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard' : "))

if difficulty== 'easy': no_of_attempts = 10 
elif difficulty =='hard': no_of_attempts = 5
else: print('Invalid Input')

comp_guessed_number = random.randint(1,100)
print(f"You have {no_of_attempts} attempts remaining to guess the number.")

if difficulty == 'easy' or difficulty == 'hard':
  while no_of_attempts and no_of_attempts > 0:
    user_guess = int(input("\nMake a guess: "))

    if user_guess == comp_guessed_number: 
      print("Congratulations! You made the perfect guess")
      break

    no_of_attempts -= 1
    
    if no_of_attempts > 0:
      comp = 'high' if user_guess > comp_guessed_number else 'low'
      print(f"Too {comp}.\nGuess again.")
      print(f"You have {no_of_attempts} attempts remaining to guess the number.")

  if no_of_attempts == 0:
    print('You are out of attempts.\nF')