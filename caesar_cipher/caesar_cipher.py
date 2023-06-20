from ast import Index
import art
print(art.logo)

def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        cipher(txt=text, shift_ammount=shift, alphabet=alphabet, dir=direction)
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restart.lower() == 'yes':
            continue
        elif restart.lower() == 'no':
            break

def cipher(txt, shift_ammount, alphabet, dir):
    end_text = ''
    try:
        alphabet.extend(alphabet)
    except:
        IndexError
    for letter in txt:
        if letter not in alphabet:
            end_text += letter  
            continue
        position = alphabet.index(letter)
        if dir == "encode":
            new_position = (position + shift_ammount) % len(alphabet)
        elif dir == "decode":
            new_position = (position - shift_ammount) % len(alphabet)
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"The {dir}d text is {end_text}")

main()





