list=[9,40,13,41,78,5,10,45,54,64,55,79,90,]
print(sorted(list))
for j in range(len(list)):
    min = list[j]
    pos_min = j
    for i in range(j + 1, len(list)):
        if list[i] < min:
            min = list[i]
            pos_min = i
    list[pos_min] = list[j]
    list[j] = min
print(min)
print(list)