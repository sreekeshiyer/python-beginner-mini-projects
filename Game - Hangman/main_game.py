import os
import random
import word_list as wl
import hangman_art as art
end_of_game = False
lives=6
chosen_word = random.choice(wl.word_list)

print(f"\n\n {art.logo} \n\n")

#Create blanks
display = []
for _ in range(len(chosen_word)):
    display += "_"

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    os.system('clear');
    # clear()
    if guess in display:
      print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")
    if guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You lost 1 life. ")
      lives -= 1
    print(art.stages[-1*(6-lives) - 1])
    
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"{' '.join(display)}")
        print("You win.")
    if lives==0:
      end_of_game=True

      print("You Lose")