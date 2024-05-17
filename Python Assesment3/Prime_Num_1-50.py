def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
n = 50
i=2
while i<=50:
    if isPrime(i):
        print(i)
    i +=1