# Method to count the digits that are divisors of the number
def findDigits(n):
    counter = 0
    d = n
    while d != 0:
        r = d % 10
        if r != 0 and n % r == 0:
            counter += 1
        d //= 10
    return counter

# Program Test
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    result = findDigits(n)
    print(result)