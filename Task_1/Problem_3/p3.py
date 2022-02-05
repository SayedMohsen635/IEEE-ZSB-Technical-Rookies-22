# A method to search the number
def binarySearch(list , right , left , searchedNum):
    mid = left + ((right - left) // 2)  # Get middle index
    while(right >= left):               # Check if right index is more than left index or not
        if(list[mid] == searchedNum):   # Check if middle number is the same as the number we want
            return mid
        if(list[mid] > searchedNum):    # Check if middle number is bigger than the number we want then we go to left subarray
            return binarySearch(list , (mid - 1) , left , searchedNum)
        if(list[mid] < searchedNum):    # Check if middle number is smaller than the number we want then we go to right subarray
            return binarySearch(list , right , (mid + 1) , searchedNum)
    else:
        return 0                        # Return false when number isn't found


# Program Test
array = [1 , 2 , 3 , 4 , 6 , 9 , 10 , 30 , 50 , 56 , 100 , 102 , 200 , 300 , 301 , 302 , 303 , 304 , 306 , 309 , 3000]

res = binarySearch(array , (len(array) - 1) , 0 , 3000)

if (res != 0):
    print("The number is found at " + str(res))
else:
    print("Number isn't found")