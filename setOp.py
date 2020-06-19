n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    c= input().split()
    if c[0] == 'pop':
        s.pop()
    elif(c[0] == 'remove'):
        s.remove(int(c[1]))
    elif(c[0] == 'discard'):
        s.discard(int(c[1]))
# print(s)
sum = 0
for i in s:
    sum += i
print(sum)