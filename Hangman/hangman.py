import hangman_art
import hangman_words
import random

def main():
    #logo
    print(hangman_art.logo)
    
    #words
    words = hangman_words.word_list

    #random word from the list
    random_word = random.choice(words)

    #word length
    word_length = len(random_word)
    
    #is the end of the game? True or False
    end_of_game = False

    #lives
    lives = 6

    #display
    display = []
    for _ in range(word_length):
        display.append("_")
    

    #loop to keep playing till the end
    while not end_of_game:
        #guess
        guess = input("Guess a letter: ").lower()
        #check if guess is in the word
        for position in range(word_length):
            letter = random_word[position]
            if letter == guess:
                display[position] = guess
        #if guess is not in random word, reduce lives by 1
        if guess not in random_word:
            print("It is not in the word. Try again!")
            lives -= 1

        #show display as hint
        print(f"{' '.join(display)}")

        #if there is no blank, the game should end (winning)
        if "_" not in display:
            print("You win!")
            end_of_game = True
        #and if lives is 0, the game should end (losing)
        if lives == 0:
            print("You lose.")
            end_of_game = True
        
        #show lives
        print(hangman_art.stages[lives])

        
main()