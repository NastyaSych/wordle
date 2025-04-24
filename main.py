import random

from words import vocab_en_words, vocab_ru_words
import utilities

# начальные строки
choose_lang = "Choose your language (en/ru):"
choose_lang_corr = "Plese, enter your language correctly!"

# строки для en mode
welcome_en = "Welcome to wordle! You have 6 attempt to guess the word."
word_request_en = "Enter your guess: "
congrats_en = "Congratulations! You guessed the word!"
bad_guess_en = "Try again!"
bad_result_en = "Unfortunately, 6 attempts were not enough for you to guess the word..."
num_attempts_en = "You have {} more attempts"
last_attempt_en = "You have the last attempt!"
leng_error_en = "Your word should consist of 5 letters!"
register_error_en = "Your word shoud consist of letters of lower register!"
not_letters_error_en = "Your word shoud consist of letters only!"
language_error_en = "You should enter word in English!"

word_ans_en = random.choice(vocab_en_words)

# строки для ru mode
welcome_ru = "Добро пожаловать в wordle! У вас есть 6 попыток, чтобы угадать слово. "
word_request_ru = "Введите ваше слово: "
congrats_ru = "Поздравляем! Вы угадали слово!"
bad_guess_ru = "Попробуйте ещё раз!"
bad_result_ru = "К сожалению, вам не хватило 6 попыток, чтобы угадать слово..."
num_attempts_ru = "У вас осталось ещё {} попытки"
num5_attempts_ru = "У вас осталось ещё 5 попыток"
last_attempt_ru = "У вас осталась последняя попытка!"
leng_error_ru = "Ваше слово должно состоять из 5 букв!"
register_error_ru = "Ваше слово должно состоять только из букв нижнего регистра!"
not_letters_error_ru = "Ваше слово должно состоять только из букв!"
language_error_ru = "Вы должны ввести слово на русском!"

word_ans_ru = random.choice(vocab_ru_words)


def en_mode(lang = "en"):
    print(welcome_en)
    for attempt in range(0, 6):
        word_guess = input(word_request_en)
        # тут должна быть функция проверки корректности ввода
        error = utilities.check_word(word_guess, lang)
        while error != 0:
            match error:
                case 1:
                    print(leng_error_en)
                case 2:
                    print(register_error_en)
                case 3:
                    print(not_letters_error_en)
                case 4:
                    print(language_error_en)
            word_guess = input(word_request_en)
            error = utilities.check_word(word_guess, lang)      
        marks_list = utilities.marks(word_guess, word_ans_en)
        utilities.painting(word_guess, marks_list)
        if marks_list == [2, 2, 2, 2, 2]:
            print('\n', congrats_en, sep='')
            break
        elif attempt == 5:
            print('\n', bad_result_en, sep='')
            break
        else:    
            print('\n', bad_guess_en, sep='')
        att_left = 6 - attempt - 1
        if att_left == 1:
            print(last_attempt_en)
        else:
            print(num_attempts_en.format(att_left)) 


def ru_mode(lang = "ru"):    
    print(welcome_ru)
    for attempt in range(0, 6):
        word_guess = input(word_request_ru)
        # тут должна быть функция проверки корректности ввода
        error = utilities.check_word(word_guess, lang)
        while error != 0:
            match error:
                case 1:
                    print(leng_error_ru)
                case 2:
                    print(register_error_ru)
                case 3:
                    print(not_letters_error_ru)
                case 4:
                    print(language_error_ru)
            word_guess = input(word_request_ru)
            error = utilities.check_word(word_guess, lang) 
        marks_list = utilities.marks(word_guess, word_ans_ru)
        utilities.painting(word_guess, marks_list)
        if marks_list == [2, 2, 2, 2, 2]:
            print('\n', congrats_ru, sep='')
            break
        elif attempt == 5:
            print('\n', bad_result_ru, sep='')
            break
        else:    
            print('\n', bad_guess_ru, sep='')
        att_left = 6 - attempt - 1
        if att_left == 1:
            print(last_attempt_ru)
        elif att_left == 5:
            print(num5_attempts_ru)    
        else:
            print(num_attempts_ru.format(att_left))              
    


def main():
    lang = ""
    while lang != "en" and lang !="ru":
        lang = input(choose_lang)
        if lang == "en":
            en_mode()
        elif lang == "ru":
            ru_mode()
        else:
            print(choose_lang_corr)    


if __name__ == "__main__":
    main()
