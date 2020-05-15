
n,m = input().split()
ele = input().split()
A = set(input().split())
B = set(input().split())
r = [(i in A) - (i in B) for i in ele]
s = 0
for i in r:
    s += i
print(s)