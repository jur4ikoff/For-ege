from  itertools import product
bad = ['АА', 'ББ', 'ВВ', 'ГГ', 'ДД']
alphabet = "АБВГД"
answ = []
for i in product(alphabet, repeat=5):
    flag = True
    for j in range(0, 4):
        if i[0] == 'A' or i[j] == i[j + 1]:
            f
print(len(answ))