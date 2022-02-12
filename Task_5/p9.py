# Method to check if the sequence has the same letters as hackerrank string or not
def hackerrankInString(s):
    list = ['h','a','c','k','e','r','r','a','n','k']
    for i in s:
        if(i == list[0]):
            list.pop(0)
        if(len(list) == 0):
            return "YES"
    return "NO"

# Program Test
n = int(input().strip())
for i in range(n):
    s = input()
    result = print(hackerrankInString(s))