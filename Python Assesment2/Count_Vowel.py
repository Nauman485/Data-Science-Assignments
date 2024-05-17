str = input("Enter your string = ")
vowel = "aeiou"
count = 0
for char in vowel:
    if char in str.lower():
        count += 1
print(f"Vowel count is = {count}")