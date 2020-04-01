a = []
n = int(input())
maxi = 0
for i in range(n):
    x = int(input())
    a.append(x)
for t in range(n):
    i = 1
    s = 0
    d = n-t
    j = t
    while(i<=d):
        for x in range(i):
            s += a[j]
            j += 1
        d -= i
        i += 1
    if(maxi<s):
        maxi = s
print(maxi)