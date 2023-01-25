alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

import art


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    alphabet_size = len(alphabet)
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > alphabet_size or new_position < 0:
                new_position = new_position % alphabet_size
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


print(art.logo)
restart = True

while (restart):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    answer = input("Do you want to restart the cipher program? [yes/no] ")
    if answer == "no":
        print("Thanks for using the cipher program, adios !")
        restart = False

