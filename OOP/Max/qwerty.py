from random import randrange

N = 100
list = []
for i in range(N):
    list.append(randrange(1, 99,))
print(list)
for i in range(N - 1):
    for j in range(N - 1 - i):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)
