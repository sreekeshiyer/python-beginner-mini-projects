from game_data import data
from art import logo, vs
import os
import random

def compare(choice_1, choice_2, user_choice):
  '''
  Make comparisons based on choice and return if your answer was correct.
  '''
  if user_choice == 'A':
    if choice_1['follower_count'] < choice_2['follower_count']: return False
    else: return True
  else:
    if choice_1['follower_count'] < choice_2['follower_count']: return True
    else: return False

score = 0
while True:
  print(logo)
  choice_1 = random.sample(data, 2)[0]
  choice_2 = random.sample(data, 2)[1]
  if score >0:
    print(f"You're right! Current Score: {score}")
  print(f"Compare A: {choice_1['name']}, a {choice_1['description']} from {choice_1['country']}")

  print(f"\n{vs}\n")

  print(f"Against B: {choice_2['name']}, a {choice_2['description']} from {choice_2['country']}")

  user_choice = input("Who has more followers? Type 'A' or 'B': ")

  if user_choice == 'A' or user_choice == 'B':
    result = compare(choice_1, choice_2, user_choice)
    
    if not result: 
      os.system('clear')
      print(logo)
      print(f"\nSorry, that's wrong. Final Score: {score}")
      break
    else:
      score += 1
      os.system('clear')
  else:
    print('Invalid Input')
    break
