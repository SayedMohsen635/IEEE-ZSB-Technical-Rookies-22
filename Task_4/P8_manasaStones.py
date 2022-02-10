# Method to find all possible values of the last stone
def stones(n, a, b):
    result = set()
    for i in range(n):
        c = (b * i) + (a * (n - i - 1))
        result.add(c)
    return sorted(result)

# Program Test
if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        print(stones(n, a, b))