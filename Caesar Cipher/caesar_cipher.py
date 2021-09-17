from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
  

def caesar_cipher(text, shift, direction): 
  final_result = ''
  if direction == 'encode': 
    check = True 
  elif direction == 'decode':
    check = False
  else: 
    print("Invalid Input")
    return

  for letter in text:

    if letter in alphabet:
      position = alphabet.index(letter)
      if check: new_position = (position + shift)
      else: new_position = (position - shift)
      final_result += alphabet[new_position]
    else: final_result += letter

  print(f"The {direction}d text is {final_result}") 
  

while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
  text = input("Type your message: \n").lower()
  shift = int(input("Type the shift value: \n"))
  shift = shift % 26
  caesar_cipher(text, shift, direction)
  choice = input ("Do you want to continue? y/n : ").lower()
  if choice == 'y': continue
  else: 
    print('\nGoodbye!')
    break