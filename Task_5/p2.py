# t --> seconds to read the book (1 ≤ t ≤ 10**6)
# n --> number of days (1 ≤ n ≤ 100)
# a[i] --> The number of seconds that she has to spend working during i-th day (0 ≤ a[i] ≤ 86400)

n , t = map(int , input().split())      # Days and time input at the same line
a = list(map(int , input().split()))    # Array input at the same line

for i in range(0 , len(a)):
    readingTime = 86400 - a[i]
    t = t - readingTime
    if(t <= 0):
        print(i + 1)
        break