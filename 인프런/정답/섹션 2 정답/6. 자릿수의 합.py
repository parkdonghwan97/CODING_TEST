# import sys  
# sys.stdin=open("input.txt","rt")
'''
자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요. 
각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.
▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자
를 출력합니다.
▣ 입력예제 1 
3
125 15232 97
▣ 출력예제 1
97

'''

# 내 코드 

n = int(input())
X = list(map(int,input().split()))
answer = []

# 자릿수의 합을 구하는 함수
def digit_sum(x):      
    tot = 0
    while True:

        if x -10 < 0 :
            tot += x
            break 
        else:
            tot += x%10 # 10으로 나눈 나머지 더함
            x = x//10   # x를 10으로 나눈 몫으로 변경

        # tot += x % 10  # x를 10으로 나눈 나머지를 합함
        # x = x // 10    # x 를 10으로 나눈 몫으로 바꿈
        # if x - 10 < 0:  # x - 10이 0인경우 탈출 
        #     break
        
    
    return tot

# 입력받은 수의 각 자리수 합을 구하는 리스트

for i in range(len(X)):
    answer.append(digit_sum(X[i]))   # 각 X 자리수 합쳐서 리스트에 추가 

# answer에서 가장 큰 값의 인덱스 추출
maxindex = 0
for i in range(len(answer)):
    if answer[i] == max(answer): # answer[i] 값이 최대값인 경우
        maxindex = i 
        break

# print(answer,maxindex)


print(X[maxindex])



