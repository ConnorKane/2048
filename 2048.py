Stop = False

r1 = [2,2,0,0]
r2 = [2,2,0,0]
r3 = [2,2,0,0]
r4 = [2,2,0,0]

c1 = [r1[0],r2[0],r3[0],r4[0]]
c2 = [r1[1],r2[1],r3[1],r4[1]]
c3 = [r1[2],r2[2],r3[2],r4[2]]
c4 = [r1[3],r2[3],r3[3],r4[3]]

rows = [r1,r2,r3,r4]
cols = [c1,c2,c3,c4]

def moveL(x):
    for i in range(0,len(x)):
        if i != 0:
            if x[i-1] == x[i]:
                x[i-1] *= 2
                x[i] = 0
        else:
            continue
        z = x.count(0)
        for i in range(1,x.count(0)):
            x.append(x.pop(x.index(0)))

def moveR(x):
    for i in range(0,len(x)):
        if i != 3:
            if x[i+1] == x[i]:
                x[i+1] *= 2
                x[i] = 0
        else:
            continue
        z = x.count(0)
        for i in range(1,x.count(0)):
            x.append(x.pop(x.index(0)))
def moveY(up):
    for col in cols:
        if up == True:
            for i in col:
                print(i)
                if col.index(i) != 0:
                    if col[i-1] == col[i]:
                        print(col[i-1],col[i])
                        col[i-1] *=2
                        col[i] = 0
        else:
            for i in col:
                if col.index != 3:
                    if col[i+1] == col[i]:
                        col[i+1] *= 2
                        col[i] = 0

