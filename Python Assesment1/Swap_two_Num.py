num1 = int(input("Enter first number = ")) 
num2 = int(input("Enter secomd number = "))
print(f"Num1 = {num1}")
print(f"Num2 = {num2}")

# Swaping number without using third variable

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

print("Values after Swap")
print(f"Num1 = {num1}")
print(f"Num2 = {num2}")