# import sys
# sys.stdin = open('input.txt')


n,m = map(int,input().split())

a = list(map(int,input().split()))
a.sort()
lt ,rt = 0, n-1 # 인덱스

# lt    mid     rt 
while  lt <=rt:
    mid = (lt+rt) // 2   #가운데 인덱스 
    if a[mid] == m :
        print(mid+1) 
        break
    elif a[mid] < m :
        lt = mid+1
    elif a[mid] > m:
        rt = mid - 1
     




