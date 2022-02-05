def sumLoop(list):          #Sum Method Using For Loop
    sum = 0
    for num in list:
        sum += num
    return sum

def sumWhile(list):         #Sum Method Using While Loop
    i = 0
    sum = 0
    while(i < len(list)):
        sum += list[i]
        i += 1
    return sum

def sumRecursion(list):     #Sum Method Using Recursion 
    if(len(list) == 1):
        return list[0]
    else:
        return list[0] + sumRecursion(list[1:])

n = input()                 #Takes Input From User
lst =list(map(int , input().strip().split()))

print(sumLoop(lst))         #Printing Results
print(sumWhile(lst))
print(sumRecursion(lst))