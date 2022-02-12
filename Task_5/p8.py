# Program to find the anagrams
n = int(input())

for i in range(n):
    s = sorted(input())
    t = sorted(input())
    S = {}  # A dictionary which has a key and its value --> (key , value)
    T = {}

    for i in s:
        S[i] = 0
    for i in t:
        T[i]=0
    for i in s:
        S[i] = S[i] + 1
    for i in t:
        T[i] = T[i] + 1

    c = 0

    for i in S:
        if i not in T:
            c = c + S[i]
        elif S[i]<T[i]:
            c = c + (T[i]-S[i])
        elif S[i]>T[i]:
            c = c + (S[i]-T[i])

    for i in T:
            if i not in S:
                c = c + T[i]
    print(c)    # Final Result