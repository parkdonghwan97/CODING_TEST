


# import sys
# sys.stdin=open("input.txt", "r")
# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 



# from statistics import mean


a= []
for i in range(10):
    a.append(int(input()))

# 평균
# print(  mean(a)  )
print(sum(a)//10)

# 최빈 값 


from collections import Counter
print(  Counter(a).most_common()  )
print(Counter(a).most_common()[0])
print(Counter(a).most_common()[0][0])


