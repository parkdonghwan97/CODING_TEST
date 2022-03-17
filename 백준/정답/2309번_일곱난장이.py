
x = []
for i in range(9):
    x.append(int(input()))

# print(x)
tot = sum(x)

a,b = 0,0

for i in range(9):

    for j in range(i+1, 9 ):
        if tot - (x[i]+x[j] ) == 100:
            a,b = x[i],x[j]
            break
x.remove(a)
x.remove(b)
x.sort()
for i in x :
    print(i)
