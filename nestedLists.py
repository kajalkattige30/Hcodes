def Convert(li) :
    dct = {li[i] : li[i+1] for i in range(0,len(li),2)}
    return dct


n = int(input())
l = []
for i in range(n):
    nl = []
    l.append(nl)
    for j in range(2):
        x = input()
        l[i].append(x)
    l[i][1] = float(l[i][1])
    # l[i].append(l[i][1])
    # print(Convert(l[i]))

# print(l)
dct = {}
Dct = {}
for i in range(len(l)):
    dct = Convert(l[i])
    Dct.update(dct)
# print(Dct)

Dct = {k: v for k, v in sorted(Dct.items(), key=lambda item: item[1])}
# print(Dct)
 
ls = [(k,v) for k,v in Dct.items()]
# print(ls)
Fl = []
for i in range(len(ls)):
    if(ls[i][1] == ls[i+1][1]):
        continue
    if(ls[i][1] < ls[i+1][1]):
        # Fl.append([])
        Fl.append(ls[i+1])
        for j in range(i+1,len(ls)):
            if(ls[j][1] == ls[j+1][1]):
                Fl.append(ls[j+1])
            else:
                break
        break
Fl.sort()
for i in range(len(Fl)):
    print(Fl[i][0])


