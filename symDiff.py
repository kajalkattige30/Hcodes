m = int(input())
mi = input().split()
ml = list(map(int, mi))
M = set(ml)

n = int(input())
ni = input().split()
nl = list(map(int, ni))
N = set(nl)

finalSet = set()
finalSet = (M.difference(N)).union(N.difference(M))
finalSet = sorted(finalSet)

for x in finalSet:
    print(x)