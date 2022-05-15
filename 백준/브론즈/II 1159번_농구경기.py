


from collections import Counter
a = int(input())
namelist = []
for i in range(a):
  namelist.append(input()[0])


tmp = dict(Counter(namelist)) 

tmp = sorted(tmp.items() ,key=lambda x: x[1] )
# print(tmp)
cnt = 0 


answer = []
for i in tmp:
  if i[1]>=5:
    cnt+=1
    answer.append(i[0])
answer.sort()
if cnt ==0:
  print('PREDAJA')
else:
  for i in answer:
    print(i,end='')


