num = int(input("Enter number = "))
a = 0
b = 1
c = 0
print(f"{a}\n{b}")
for i in range(2,num):
    c = a+b
    a = b
    b = c
    print(f"{c}")