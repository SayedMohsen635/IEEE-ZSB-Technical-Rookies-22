# Function To Calculate The Number Of r's
def repeatedLetter(str , num):
    r = num % len(str)
    m = (num - r) / len(str)
    count = 0
    for i in range(len(str)):
        if (str[i] == "a"):
            count += int(m + (i < r))
    return count

# Program Test
str = input()
n = int(input())
print(repeatedLetter(str , n))