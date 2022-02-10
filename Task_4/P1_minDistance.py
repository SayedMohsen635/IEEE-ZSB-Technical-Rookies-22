# Method To Find The Minimum Number In List
def minNumber(list):
    min = list[0]
    for i in range(0 , len(list)):
        if(list[i] < min):
            min = list[i]
    return min

# Method To Find The Minimum Distance Between Two Similar Numbers
def minDistance(list):
    arr = []
    for i in range(0 , len(list)):
        for j in range(i + 1 , len(list)):
            if(list[i] == list[j]):
                result = abs(i - j)
                arr.append(result)
    if not arr:
        return "No Similar Numbers"
    else:
        return(minNumber(arr))

# Program Test
arr = list(map(int , input().strip().split()))
print(minDistance(arr))