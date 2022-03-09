# import sys  
# sys.stdin=open("input.txt","rt")
'''
뒤집은 소수
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 
프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력
한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하
여 프로그래밍 한다.
▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 100,000를 넘지 않는다.
▣ 출력설명
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.
▣ 입력예제 1 
5
32 55 62 3700 250
▣ 출력예제 1
23 73


'''
import re
import sys  


# 내 코드 
n = int(input())
X = list(map(int,input().split()))
answer = []

# 뒤집는 함수
def reverse(x):  #   31   => 13
    cnt = 0
    tot = 0 
    M = list()
    while True:
        M.append(x % 10) #  1의 자리수 구하기
        if x - 10 < 0 :  # 1의 자리수 인경우
            break
        else:              # 10의 자리수 이상인 경우
            x = x //10     # x를 10의 몫으로 변경
            
            cnt += 1       # cnt의 개수 증가
    cnt = len(M)                                         #  와 코드 개더럽네진짜
    for i in M:
        cnt -=1
        tot += i* 10**cnt
    return tot 
  

# # 소수인지 확인하는 함수 
def isPrime(x):
    # 아 이거 어제 했던 건데......
    cnt = 0
    for i in range(1,x+1):
        if x % i ==0:
            cnt +=1
    # 5 % 1 == 0
    # 5 % 2 == 1
    # 5 % 2 == 2
    # 5 % 3 == 3
    # 5 % 4 == 4
    # 5 % 5 == 0 
    if cnt == 2 :
        return x

for i in X:   # X = list(int(input()))
    if isPrime(reverse(i))!=None:
        print(reverse(i),end=' ')



