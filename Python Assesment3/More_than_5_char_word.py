lst = ["Aman","Sharma","Nauman","Abhijeet","Shailendra","Suraj"]
count = 0
for i in range(int(len(lst))):
    if len(lst[i])>5:
        count +=1
print(count)