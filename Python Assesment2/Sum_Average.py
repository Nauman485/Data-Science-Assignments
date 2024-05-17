lst = [45,12,34,2,56,4,67]
sum = 0
for i in range(0,int(len(lst))):
        sum = sum + lst[i]
avg = sum/int(len(lst))
print(lst)
print(f"Sum = {sum}")
print(f"Average = {avg}")