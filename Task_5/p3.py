# Method to rotate the array and return the list which has the values of the required elements
def circularArrayRotation(a, k, queries):
    list = []
    k %= len(a)
    for q in queries:
        element = len(a) - k + q
        list.append(a[element % len(a)])
    return list


# Program Test
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
q = int(first_multiple_input[2])
a = list(map(int, input().rstrip().split()))
queries = []

for _ in range(q):
    queries_item = int(input().strip())
    queries.append(queries_item)

print(circularArrayRotation(a, k, queries))