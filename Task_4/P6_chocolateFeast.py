# Method to count the chocolate eaten
def chocolateFeast(n, c, m):
    # every eatenChocolate, he will have 1 wrapper
    # then number of eatenChocolate = number of wrappers
    eatenChocolate = wrappers = n // c
    while wrappers >= m:
        newChocolates = wrappers // m
        eatenChocolate += newChocolates
        wrappers = (wrappers % m) + newChocolates
    return eatenChocolate

# Program Test
t = int(input().strip())
for i in range(t):
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    print(chocolateFeast(n, c, m))