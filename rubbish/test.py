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
print(letter)
