 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();



def DFS(L,p):   
    global cnt 
    if L==n:
        cnt+=1
        for i in range(p) : 
            # print(answer[i]  ,end=' ')
            # print( str(answer[i] +64 ) ,end='' )
            print( chr(answer[i] +64 ) ,end='' ) # 숫자 => 문자 
        print()

    else:
        # for i in range(len(code)) # 1 부터 시작해야됨 , 알파벳 고정 되어있음.
        for i in range(1,27):
            if code[L] == i  : # 
                answer[p] = i  
                DFS(L+1, p+1)

            elif i>=10 and code[L] == i//10 and code[L+1] == i % 10 :
                answer[p] =i
                DFS(L+2,p+1)


'''
answer= [2 5 1 1 4 ]
answer= [25 1 1 4 ]  --- 

'''



# A = 1 ~  Z = 26

code = list(map(int, input() ))

n = len(code)   # 종착점 
code.insert(n,-1)    # 마지막 위치에 -1 추가   마지막 2자리 계산용
answer = [0] *(n+3)
cnt= 0 
DFS(0,0)
print(cnt)