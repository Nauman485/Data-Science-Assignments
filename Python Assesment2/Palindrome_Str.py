def isPalindrome(str):
    for i in range(0,int(len(str)/2)):
        if str[i] != str[len(str)-(i+1)]:
            return False
    return True
Str= input("Enter your string = ")
ans = isPalindrome(Str)
if ans:
    print(f"{Str} is Palindrome string")
else:
    print(f"{Str} is not Palindrome string")