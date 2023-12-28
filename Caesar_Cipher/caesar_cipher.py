import caesar_cipher_art
import string
def main():
    #logo
    print(caesar_cipher_art.logo)

    #end or not?
    is_end = False

    #alphabet
    letters = string.ascii_lowercase

    while not is_end:
        #direction
        direction = input("Type 'encode' to encode, or 'decode' to decode: ").lower()

        #text
        text = input("Text: ").lower()

        #shift
        shift = int(input("Shift: "))

        #caesar()
        print(f"The {direction}d text: {caesar(plain_text=text, key=shift, alphabets=letters,directions=direction)}")

        #ask users if they want to use it again
        is_end = input("Do you want to use it again? yes or no? ").lower()
        if is_end == "yes":
            is_end = False
        elif is_end == "no":
            is_end = True

    
    


def caesar(plain_text, key, alphabets, directions):
    """
    For each letter in plain_text, if it is in english alphabets, shift its position based on keys
    Encoding => position + key
    Decoding => position - key
    """
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            if directions == "encode":
                new_position = position + key
                if new_position > 25:
                    new_position %= 26
            elif directions == "decode":
                new_position = position - key
            cipher_text += alphabets[new_position]
        else:
            cipher_text += letter
    return cipher_text



                






























main()












