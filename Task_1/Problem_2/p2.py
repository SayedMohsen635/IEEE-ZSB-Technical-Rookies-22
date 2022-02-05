# A function to check if number is prime or not
def primeNumber(n):
    if(n % 2 == 0 and n != 2):
        return 0
    if(n == 2):
        return 1
    for x in range(3 , n):
        if((n % x == 0) and (n != x)):
            return 0
    return 1

# Takes number from user
number = int(input())

# A loop to print all prime numbers less than number taken from user
for x in range(2 , (number + 1)):
    if(primeNumber(x) == 1):
        print(x , end = " ")   # The (end) makes the values printed in the same line