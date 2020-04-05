mainList = []

x = int(input())
y = int(input())
z = int(input())
n = int(input())
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            l = []
            s = i+j+k
            if(s != n):
                l.extend((i,j,k))
                mainList.append(l)
print(mainList)
