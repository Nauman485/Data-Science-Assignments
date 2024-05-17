lst = [45,12,-4,2,56,-25,67,-57]
sum = 0
for i in range(0,int(len(lst))):
    if lst[i] > 0 :
        sum = sum + lst[i]
print(lst)
print(f"Sum of all positive number of list is = {sum}")
