# import sys  
# sys.stdin=open("input.txt","rt")
'''
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
'''



n = int(input())

score = list(map(int,input().split()))

ScoreMean = int(round(sum(score) / len(score),0))
# avg(score) 이게 없나??

answer = [] 
for i in score:
    answer.append(i - ScoreMean)

minidex = 0 
for i in range(len(answer)):
    if answer[i]<0  :
        answer[i] = 9999 # 0보다 작은 친구들을 999로 만들고  최소값을 뽑는거임!
    if answer[i] == min(answer):
        minidex =i 


# 10
# 45 73 66 87 92 67 75 79 75 80
# print(answer)
# print(min(answer))
print(ScoreMean, minidex-1)