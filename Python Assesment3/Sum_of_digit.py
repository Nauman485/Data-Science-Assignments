num = int(input("Enter your digit = "))
sum = 0;
while num>0:
    r = num%10
    sum = sum+r
    num = num//10
print(f"Sum of digit is {sum}")
