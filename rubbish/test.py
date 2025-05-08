import numpy as np

slovo = []
for i in range(0, 5):
    slovo.append([])

slovo[0].append("a")
slovo[0].append("b")
slovo[1].append("a")
# print(slovo[0][1])

letter = np.empty((5, 5), dtype=object)
letter[0, 1] = 1
letter[1, 0] = 2

letter = [[None] * 5] * 5  # строки при присвоении дублируются

letter = [[None for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        letter[i][j] = f"{i}{j}"

word_ans = "apple"
word_guess = "lelle"
marks_list = [0 for i in range(5)]
word_ans_copy = [x for x in word_ans]
# сначала находим полное совпадение и удаляем эти буквы
for letter in range(5):
    if word_guess[letter] == word_ans_copy[letter]:
        marks_list[letter] = 2
        word_ans_copy[letter] = " "
# смотрим на оставшиеся буквы
for letter in range(5):
    if marks_list[letter] != 2:
        for true_letter in range(5):
            if (
                word_guess[letter] == word_ans_copy[true_letter]
                and true_letter != letter
            ):
                marks_list[letter] = 1
                word_ans_copy[true_letter] = " "
# print(word_ans_copy)
print(marks_list)
