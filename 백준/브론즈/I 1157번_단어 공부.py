




from collections import Counter

a = input()
a = a.upper()
answer= [] 

for i in range(len(a)):
  answer.append(a[i])

tmp = dict(Counter(answer))

tmp = sorted(tmp.items(), key=lambda x: x[1] , reverse=True )


if len(tmp) >= 2:

  if tmp[0][1] ==tmp[1][1]:
    print("?")
    exit()

print(tmp[0][0])


