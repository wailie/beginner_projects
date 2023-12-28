import random

def main():
    
    #print greeting to users
    print("Welcome to the Number Guessing Game!")

    #hint
    print("I am thinking of a number between 1 and 100.")
    
    #attempt for easy
    attempt = 10
    
    #number list
    numbers = []
    
    #adding numbers to list
    for n in range(1, 100 + 1):
        numbers.append(n)
    
    #random number
    random_number = random.choice(numbers)
    
    #asking easy or hard
    difficulty = input("Choose Difficulity (easy or hard): ").lower()

    #game start
    number_guessing_game(difficulty, random_number, attempt)






def number_guessing_game(difficulties, number, attempts_left):
    """
    ***** Number Guessing Game Function *****
    # takes in difficulty and random number
    # check if difficulty is easy or hard
    # if difficulty is easy, remaining attempts are 10
    # else if difficulty is hard, remaining attempts are 5
    # check if guess is correct
    # if guess is correct, print "You got it!"
    # else lose 1 attempts each time
    # when attempts are over, print "You lose!"
    """
    # if difficulties == "easy":
    #     attempts_left = 10
    # else:
    #     attempts_left = 5
    attempts_left = 10 if difficulties == "easy" else 5 #Ternary Operator

    while True:
        if attempts_left == 0:
            print("You've run out of guesses, you lose.")
            break
        elif attempts_left > 0:
            print(f"You have {attempts_left} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f"You guessed it! The answer was {number}.")
                break
            else:
                attempts_left -= 1
                compare(guess, number, attempts_left)
                continue



def compare(guess, number, attempts_left):
    #Compare guess and number and give hints
    if guess > number and attempts_left != 0:
        print("Too high!\nTry again.")
    elif guess < number and attempts_left != 0:
        print("Too low!\nTry again.")
    elif guess > number and attempts_left == 0:
        print("Too high!")
    elif guess < number and attempts_left == 0:
        print("Too low!")



main()