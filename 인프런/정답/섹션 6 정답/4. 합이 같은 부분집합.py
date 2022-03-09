# import sys
# sys.stdin = open('input.txt')

import sys
# 부분집합 구하기 

# def DFS(L, sum):   # L : a리스트 접근하는 인덱스 ( LEVEL )


#     # 레벨을 올림,    sum을 합칠지, 말지

#     # 종료는? a 리스트를 벗어날때
#     if L == n : 
#         if sum == (total - sum):  # sum이랑 전체값 - sum 가 같으면 
#             print('YES')
#             sys.exit(0)
#     else:
#         DFS(L+1, sum+a[L])
#         DFS(L+1, sum )  


# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int,input().split()))
#     total = sum(a)
#     DFS(0, 0)        
#     print('NO')



# 시간 복잡도 생각해서 더 좋은 코드 

# total //2 보다 넘어가면 굳이 가지 뻗을 필요가 없음



def DFS(L, sum):   # L : a리스트 접근하는 인덱스 ( LEVEL )

    if sum > total // 2:
        return

    # 레벨을 올림,    sum을 합칠지, 말지

    # 종료는? a 리스트를 벗어날때
    if L == n : 
        if sum == (total - sum):  # sum이랑 전체값 - sum 가 같으면 
            print('YES')
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum )  


if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    DFS(0, 0)        
    print('NO')