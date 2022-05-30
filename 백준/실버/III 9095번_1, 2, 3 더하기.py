

# III 9095번_1, 2, 3 더하기

def sol(x):
    if x ==1 :
        return 1
    elif x ==2 :
        return 2
    elif x ==3 :
        return 4
    else:
        return sol(x-1) +sol(x-2) +sol(x-3)


n = int(input())

for i in range(n):
    a = int(input())
    print(sol(a))






'''
1   1
2   11 2
3   11 12 21  3
4   1111 112 121 211 31 13 4

a[n] = a[n-1]+a[n-2]+a[n-3]  재귀 ( dp 쓰는 문제)
'''