#Treasure Island Game
#Basic Use of if-else conditionals. 


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_choice = input('''You're at a cross road. Where do you want to go? Type "left" or "right" to choose.\n''')


while True:
  if first_choice == "left":
    second_choice = input('''\n-----------------------------\nYou come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n''')
    if second_choice == "wait":
      third_choice=input('''\n-----------------------------\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n''')
      if third_choice=="red":
        print("You were burned by fire. Game Over.")
        break
      elif third_choice=="blue":
        print("You were eaten by beasts. Game Over. They had a good dinner though.")
        break
      elif third_choice=="yellow":
        print("You found the treasure chest! You Win!")
        break
      else:
        print("Game Over.")
        break
    else:
      print('You were attacked by a trout. Game Over. ')
      break
  else:
    print('You fell into a hole. Game Over.')
    break
  