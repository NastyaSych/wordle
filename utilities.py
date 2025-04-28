import rich


def marks(word_guess: str, word_ans: str) -> list:
    # 2 - буква на основном месте
    # 1 - буква есть в слове, но не на этом месте
    # 0 - остальное
    marks_list = [0 for elem in range(5)]
    word_ans_copy = [x for x in word_ans]
    for letter in range(0, 5):
        if word_guess[letter] == word_ans_copy[letter]:
            marks_list[letter] = 2
            word_ans_copy[letter] = " "
    for letter in range(0, 5):
        if marks_list[letter] != 2:
            for true_letter in range(0, 5):
                if word_guess[letter] == word_ans_copy[true_letter]:
                    marks_list[letter] = 1
                    word_ans_copy[true_letter] = " "
    return marks_list


def painting(word_guess: str, marks_list: list):
    for order in range(0, 5):
        if marks_list[order] == 2:
            rich.print(f"[white on green]{word_guess[order]}", end="")
        elif marks_list[order] == 1:
            rich.print(f"[white on yellow]{word_guess[order]}", end="")
        else:
            rich.print(f"[white on black]{word_guess[order]}", end="")


def check_word(word_guess: str, loc) -> int:
    # 0 - без ошибок
    # 1 - неподходящая длина слова
    # 2 - неподходящий регистр
    # 3 - есть небуквенные символы
    # 4 - неподходящий язык
    if len(word_guess) != 5:
        return 1
    if not word_guess.islower():
        return 2
    if not word_guess.isalpha():
        return 3
    alph = loc["alph"]
    check = [x for x in word_guess if x in alph]
    if len(check) != 5:
        return 4
    return 0
