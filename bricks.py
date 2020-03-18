n = int(input())
i = 1
while(n>0):
    if(n == 1 or n<i):
        p = n
        n -= n  
        m = 0      
    else:       
        p = i
        n -= p
        if(n >= 2*p):
            m = 2*p
            n -= m
        else:
            m = n
            n -= n
        i += 1

if(m == 0):
    print("Patlu")
else:
    print("Motu")