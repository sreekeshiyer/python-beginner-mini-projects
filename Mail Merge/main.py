from os import path


with open('.\\Input\\Letters\\starting_letter.txt', mode="r") as file:
    mail_content = file.read()

with open('.\\Input\\Names\\invited_names.txt', mode="r") as file:
    names = (file.read()).split('\n')

for name in names:
    path = ".\\Output\\ReadyToSend\\letter_for_"+name+".txt"
    with open(path, mode="w") as file:
        file.write(mail_content.replace("[name]", name))
