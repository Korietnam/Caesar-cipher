import art
from letters_numbers_symbols import l_n_s

def caesar(start_text, shift_amount, cipher_direction):
    translated_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in l_n_s:
            position = l_n_s.index(char)
            new_position = (position + shift_amount) % len(l_n_s)
            translated_text += l_n_s[new_position]
        else:
            translated_text += char
    print(f"The {cipher_direction}d text is {translated_text}")

print(art.logo)

try_again = True
while try_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    execute_again = input(f"Would you like to try again? ").lower()
    if execute_again == "no":
        try_again = False