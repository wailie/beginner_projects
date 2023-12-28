import random
def main():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "P", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = [ "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "=", ":", "?"]

    letter_length = int(input("How many letters would you like? "))
    number_length = int(input("How many numbers would you like? "))
    symbols_length = int(input("How many symbols would you like? "))

    password_list = []
    password = ""

    for _ in range(letter_length):
        password_list.append(random.choice(letters))
    
    for _ in range(number_length):
        password_list.append(random.choice(numbers))

    for _ in range(symbols_length):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    for char in password_list:
        password += char

    print(password)

main()

