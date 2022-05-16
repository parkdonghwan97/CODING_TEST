
# from itertools import combinations
# from collections import Counter
# s1,s2,s3 = map(int,input().split())
# a1=[]
# a2=[]
# a3=[]
# for i in range(1,s1+1):
#     a1.append(i)
# for i in range(1,s2+1):
#     a2.append(i)
# for i in range(1,s3+1):
#     a3.append(i)


# tmp = []
# for i in a1:
#     for j in a2:
#         for k in a3:
#             tmp.append(sum([i,j,k]))
# print(tmp)
# mydict =dict(Counter(tmp))
# x = sorted(mydict.items(), key=lambda x: x[1] , reverse=True )

# print(x[0][0])

# 다른사람 코드 
# a,b = input().split()
# print( sum(map(int,a)) *sum(map(int,b))  )

# 다른사람 코드2 
a,b,c = map(int,input().split())

s = [0] * 81
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            s[i+j+k] += 1 
print(s.index(max(s)))