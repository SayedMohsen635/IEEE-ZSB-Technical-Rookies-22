# Method to calculate the maximum badget spend in shop
def getMoneySpent(keyboards, drives, b):
    list = []
    for j in range(0 , len(keyboards)):
        for k in range(0 , len(drives)):
            total = keyboards[j] + drives[k]
            if(total <= b):
                list.append(total)
    if not list:
        print(-1)
    else:
        print(max(list))

# Program Test
if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)