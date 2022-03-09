# import sys  
# sys.stdin=open("input.txt","rt")
'''
소수(에라토스테네스 체)
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다. 
▣ 입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
▣ 출력설명
첫 줄에 소수의 개수를 출력합니다.
▣ 입력예제 1 
20
▣ 출력예제 1
8


'''
import sys  


# 내 코드 

# 제한시간이 달려있어서 살짝 쫄리는데 암튼


# n = int(sys.stdin.readline())
# answer = 0
# for i in range(1,n+1):
#     cnt = 0
#     for j in range(1, i+1):
#         # print(i, j )
        
#            # 소수의 개수  는 2개여야함 1과 자기 자신
#         if i % j == 0: # 나눠 떨어지면 + 1
#             cnt += 1
#     # print("================")
#     if cnt == 2 :
#         answer+=1
# print(answer)
########################################################
# num=set(range(2,n+1))

#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
########################################################## 실패 

# 정답

#  2 의 배수는 정답이 될 수 없다.! 

n = int(input())
ch = [0]  * (n+1)   #  n+1개 만큼 0을 만듬
cnt = 0

for i in range(2,n+1) :  # 2부터 n 까지  
    if ch[i] == 0 :
        cnt +=1
        for j in range(i , n+1, i ):  #  i부터 n까지 i배수만큼 
            ch[j] = 1
print(cnt)






