list = [30, 20, 25, 1, 5, 35,213,34,12,54,45,21]
print(sorted(list))
for j in range(len(list)):
    min = list[j]
    pos_min = j
    for i in range(j+1,len(list)):
        if list[i] < min:
            min = list[i]
            pos_min = i
    list[pos_min] = list[j]
    list[j] = min
print(min)
print(list)
