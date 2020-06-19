from collections import Counter
k = int(input())
rl = input().split()
c = Counter(rl)
l = list(c.items())
for i in l:
    if(i[1] == 1):
        print(i[0])