from random import randbytes

n = 100
list = []
for i in range(n):
    list.append(randbytes(1, 1000))
print(list)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)
