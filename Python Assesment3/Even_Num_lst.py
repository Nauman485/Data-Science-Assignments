lst = [24,45,68,20,47,28,35,56]
lst1 =[]
for i in range(int(len(lst))):
    if lst[i]%2 == 0:
        lst1.append(lst[i])
print(lst1)