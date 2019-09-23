import math

def isPrime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5 + 1), 2):
            if n % i == 0:
                return False
        return True

number = 3
primes = [2]

while (True):
    if isPrime(number):
        primes.append(number)
    else:
        for i in primes:
            if math.sqrt(((number - i) / 2)) == int(math.sqrt(((number - i) / 2))):
                break
        else:
            print(number)
            break
    number += 2        
