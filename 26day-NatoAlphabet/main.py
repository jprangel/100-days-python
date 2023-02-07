import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for index,row in nato.iterrows()}
word = input("Enter a word: ").upper()
nato_word = [nato_alphabet_dict[l] for l in word]
print(nato_word)
