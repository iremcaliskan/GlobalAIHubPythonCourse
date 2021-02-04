"""
    Finding prime numbers between 0 and 100 using functions
"""
# Prime() finds prime nums btw 0 and 100
def Prime():
    for num in range (0,101):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                print(num)
Prime()

# TakeRange() finds prime nums in Interval that lower and upper ranges are determined by users 
lowerRange = int(input("Enter lower range: "))  
upperRange = int(input("Enter upper range: "))

print(f'\nPrime numbers between {lowerRange} and {upperRange} are:')
def TakeRange(lowerRange,upperRange ):
    for num in range(lowerRange,upperRange + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:  
                print(num)  
TakeRange(lowerRange,upperRange)

# isPrime() prints single number that is prime or not
def isPrime(num):
    if num>1:
        for i in range(2, num + 1):
            if num % i == 0 and i != num :
                print(f'{num} is not a prime number.')
                break
            else :
                print(f'{num} is a prime number.')
                break
    else:
        print(f'{num} is not a prime number.')
isPrime(2)