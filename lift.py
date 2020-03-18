t = int(input())
a = 0
b = 7
for i in range(t):
    n = int(input())
    if((n-a) <= (b-n)):
        a = n
        print("A")
    else:
        b = n
        print("B")
    
