# import sys
# sys.stdin = open('input.txt')


# 부분집합 구하기 





# def DFS(v):
#     if v > n:
#         for i in range(1,n+1):
#             if check[i] == 1 : # 인덱스 값이 1인경우 i출력
#                 print(i,end=' ')
#         print()
#     else:



#         check[v] = 1 
#         DFS(v + 1)
#         check[v] = 0
#         DFS(v + 1)

# if __name__=="__main__":
#     n = int(input())
#     check=[0] * (n+1)
#     DFS(1)


def DFS(v):                                      # 1 
    if v > n:                                 
        for i in range(1,n+1):
            
            if check[i] == 1: 
                print(i, end= ' ')
        print()
    else:                                  

        check[v] = 1          #  원소를 사용 하고 다음 원소로 넘어감.
        DFS(v+1)

        check[v] = 0          #  원소를 사용 안하고 다음 원소로 넘어감.
        DFS(v+1)


if __name__ == '__main__':

    n = int(input())
    check = [0] * (n+1)
    DFS(1)


#[1 0 0 0] v = 1   DFS(2)
#[1 1 0 0] v = 2   DFS(3)
#[1 1 1 0] v = 3   DFS(4)
# v > n  - > 출력 1 2 3 
#[1 1 0 0]      v =     DFS(3)-> check[v] = 0  DFS(v+1)
# v> n - > 출력 1 2 
#v=2 -> DFS(3)  -> check[i] = 1 DFS(v+1)  = [1 0 1 0 ] -> DFS(4)
# v> n -> 출력 1 3 
# v= 2 check[i] = 0 DFS(v+1)
#[1 0 0 0 ] v= 4
# v>n -> 출력 1 


 # 이거 맞나??

