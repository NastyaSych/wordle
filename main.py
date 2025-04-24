import random

from words import vocab_words
import utilities

welcome_str = "Welcome to wordle! You have 6 attempt to guess the word. Enter your guess: "
congrats_str = "Congratulations! You guessed the word!"
bad_guess_str = "Try again!"
bad_result_str = "Unfortunately, 6 attempts were not enough for you to guess the word..."

word_ans = random.choice(vocab_words)

def main():
    print(welcome_str)
    for attempt in range(0, 5):
        word_guess = input()
        marks_list = utilities.marks(word_guess, word_ans)
        utilities.painting(word_guess, marks_list)
        if marks_list == [2, 2, 2, 2, 2]:
            print('\n', congrats_str, sep='')
            break
        elif attempt == 4:
            print('\n', bad_result_str, sep='')
        else:    
            print('\n', bad_guess_str, sep='')
    




if __name__ == "__main__":
    main()
