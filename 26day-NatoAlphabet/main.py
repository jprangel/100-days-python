import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for index,row in nato.iterrows()}

def generate_phonetic_word():
    word = input("Enter a word: ").upper()
    try:
        nato_word = [nato_alphabet_dict[l] for l in word]
    except KeyError:
        print(f"Sorry {word} is invalid, only letter in the latin alphabet are allowed")
        generate_phonetic_word()
    else:
        print(nato_word)

generate_phonetic_word()