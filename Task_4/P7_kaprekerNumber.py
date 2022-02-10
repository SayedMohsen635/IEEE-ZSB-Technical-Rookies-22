# Method to find all kaprekarNumbers
def kaprekarNumbers(p , q):
    list = []
    for n in range(p , q + 1):
        d = 10 ** len(str(n))
        l = (n ** 2) // d
        r = (n ** 2) % d
        if l + r == n:
            list.append(n)
    if list:
        print(*list)
    else:
        print("INVALID RANGE")

# Program Test
if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)