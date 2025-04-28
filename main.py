import random
from localization import langs
from words import vocab_en_words, vocab_ru_words
import utilities

# начальные строки
choose_lang = "Choose your language (en/ru):"
choose_lang_corr = "Plese, enter your language correctly!"

word_ans_en = random.choice(vocab_en_words)

word_ans_ru = random.choice(vocab_ru_words)


def en_mode(lang = "en"):
    print(langs(lang, "welcome"))
    for attempt in range(0, 6):
        word_guess = input(langs(lang, "word request"))
        # тут должна быть функция проверки корректности ввода
        error = utilities.check_word(word_guess, lang)
        while error != 0:
            match error:
                case 1:
                    print(langs(lang, "leng error"))
                case 2:
                    print(langs(lang, "register error"))
                case 3:
                    print(langs(lang, "not letters error"))
                case 4:
                    print(langs(lang, "language error"))
            word_guess = input(langs(lang, "word request"))
            error = utilities.check_word(word_guess, lang)      
        marks_list = utilities.marks(word_guess, word_ans_en)
        utilities.painting(word_guess, marks_list)
        if marks_list == [2, 2, 2, 2, 2]:
            print('\n', langs(lang, "congrats"), sep='')
            break
        elif attempt == 5:
            print('\n', langs(lang, "bad result"), sep='')
            break
        else:    
            print('\n', langs(lang, "bad guess"), sep='')
        att_left = 6 - attempt - 1
        if att_left == 1:
            print(langs(lang, "last attempt"))
        else:
            print(langs(lang, "num attempts").format(att_left)) 


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
