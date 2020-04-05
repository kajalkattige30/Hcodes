l = []
n = int(input())
for i in range(n):
    x = int(input())
    l.append(x)
l.sort(reverse=True)
for i in range(0,len(l)-1):
    if(l[i] > l[i+1]):
        r = l[i+1]
        break
print(r)