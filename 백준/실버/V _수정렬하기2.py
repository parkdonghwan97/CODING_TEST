

# V _수정렬하기2
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
a = list(set(a))
for i in a:
    print(i)
# print(a)