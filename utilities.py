import rich


def marks(word_guess: str, word_ans: str) -> list:
    # 2 - буква на основном месте, 1 - буква есть в слове, но не на этом месте, 0 - остальное
    marks_list = [0 for elem in range(5)]
    for order in range(0, 5):
        if word_guess[order] == word_ans[order]:
            marks_list[order] = 2
        else:
            for set in range(0, 5):
                if word_guess[order] == word_ans[set] and order != set:
                    marks_list[order] = 1
                    break
    return marks_list


def painting(word_guess: str, marks_list: list):
    for order in range(0, 5):
        if marks_list[order] == 2:
            rich.print(f'[white on green]{word_guess[order]}', end='')
        elif marks_list[order] == 1:
            rich.print(f'[white on yellow]{word_guess[order]}', end='')
        else:
            rich.print(f'[white on black]{word_guess[order]}', end='')
