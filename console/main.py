import random

import utilities
from localization_main import localization as lc


def mode(loc):
    word_ans = random.choice(loc["vocab"])
    print(loc["message"]["welcome"])
    for attempt in range(0, 6):
        word_guess = input(loc["message"]["word request"])
        # тут должна быть функция проверки корректности ввода
        error = utilities.check_word(word_guess, loc)
        while error != 0:
            match error:
                case 1:
                    print(loc["message"]["leng error"])
                case 2:
                    print(loc["message"]["register error"])
                case 3:
                    print(loc["message"]["not letters error"])
                case 4:
                    print(loc["message"]["language error"])
            word_guess = input(loc["message"]["word request"])
            error = utilities.check_word(word_guess, loc)
        marks_list = utilities.marks(word_guess, word_ans)
        utilities.painting(word_guess, marks_list)
        if marks_list == [2, 2, 2, 2, 2]:
            print("\n", loc["message"]["congrats"], sep="")
            break
        elif attempt == 5:
            print("\n", loc["message"]["bad result"], sep="")
            break
        else:
            print("\n", loc["message"]["bad guess"], sep="")
        att_left = 6 - attempt - 1
        if att_left == 1:
            print(loc["message"]["last attempt"])
        else:
            print(loc["message"]["num attempts"].format(att_left))


def main():
    lan = ""
    while lan != "eng" and lan != "ru":
        lan = input(lc["eng"]["message"]["choose lang"])
        if lan == "eng" or lan == "ru":
            mode(lc[lan])
        else:
            print(lc["eng"]["message"]["choose lang corr"])


if __name__ == "__main__":
    main()
