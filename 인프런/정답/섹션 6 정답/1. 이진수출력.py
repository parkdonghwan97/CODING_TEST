# import sys
# sys.stdin = open('input.txt')






def ToBin(x):

    if x == 0 :
        return    # n인경우 종료 

    # else:
    #     print(x%2, end = ' ')  # 나머지를 출력하고
    #     ToBin(x//2 ) # 몫을 재귀

# 이걸 반대로 출력해야됨. -> 
    else:
        ToBin(x//2 ) 
        print(x%2, end = ' ')    # 호출 후 프린트 
        



n = int(input())

ToBin(n)


'''
if __name__ =='main':
    n = int(input())
    ToBin(n)

'''
# stack = [ToBin(11) ToBin(5) ToBin(2)  ToBin(1) ]
