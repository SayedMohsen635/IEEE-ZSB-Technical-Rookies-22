# Method to delete less popularity friends
def Delete(k , Friends):
    temp = []
    for i in Friends:
        while(len(temp) > 0 and temp[-1] < i and k > 0):
            temp.pop()
            k -= 1
        temp.append(i)
    return temp

# Program Test
element = int(input())
for i in range(element):
    n , k = map(int , input().split())
    Friends = list(map(int, input().split()))
    print(*Delete(k , Friends))