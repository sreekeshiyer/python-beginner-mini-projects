import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_words_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word: ").upper()

final_list = [phonetic_words_dict[letter] for letter in word]

print(final_list)
