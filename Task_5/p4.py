# Method to find the beautifulTriplets in an array
def beautifulTriplets(d, arr):
    beautiful_triplets = 0
    for i in range(0 , len(arr)):
        if((arr[i] + d) in arr and (arr[i] + (2 * d)) in arr):
            beautiful_triplets += 1
    return beautiful_triplets

# Program Test
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
print(beautifulTriplets(d, arr))