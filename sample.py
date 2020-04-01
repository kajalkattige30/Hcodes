""" s = input()
kevin = []
stuart = []
subs = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s) + 1)]
for x in subs:
    if(x[0] in ['a','e','i','o','u']):
        kevin.append(x)
    else:
        stuart.append(x)
if(len(kevin) > len(stuart)):
    print("Kevin", len(kevin))
elif(len(stuart) > len(kevin)):
    print("Stuart", len(stuart))
else:
    print("Draw")
 """
def minion_game(string):
# your code goes here
    kevin = []
    stuart = []
    subs = [string[i:j] for i in range(len(string)) for j in range(i+1, len(string) + 1)]
    for x in subs:
        if(x[0] in ['a','e','i','o','u']):
            kevin.append(x)
        else:
            stuart.append(x)
    if(len(kevin) > len(stuart)):
        print("Kevin", len(kevin))
    elif(len(stuart) > len(kevin)):
        print("Stuart", len(stuart))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

    # l = []
# n = int(input())
# for x in range(n):
#     command = input()
#     if(command == 'insert'):
#         e = int(input())
#         i = int(input())
#         l.insert(i,e)       
#     elif(command == 'print'):
#         print(l)
#     elif(command == 'remove'):
#         e = int(input())
#         l.remove(e)
#     elif(command == 'append'):
#         e = int(input())
#         l.append(e)
#     elif(command == 'sort'):
#         l.sort()
#     elif(command == 'pop'):
#         l.pop()
#     elif(command == 'reverse'):
#         l.reverse()
#     else:
#         pass