# import sys  
# sys.stdin=open("input.txt","rt")
'''
정다면체
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

▣ 입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
▣ 출력설명
첫 번째 줄에 답을 출력합니다.
▣ 입력예제 1 
4 6
▣ 출력예제 1
5 6 7
'''


# 내 코드 
N,M = map(int,input().split()) # N, M 은  4 6 8 12 20 면체 중  하나

hap = []

for i in range(1,N+1):
    for j in range(1, M+1):
        hap.append(i+j)  # N + M값을 모두 더해서 리스트에 추가함 

fre = []
answer = []
for i in range(len(hap)):
    fre.append(hap.count(hap[i]))
    
for i in range(len(fre)):
    if fre[i] == max(fre):     # 빈도수의 i번째 인덱스가  최대 빈도수 인경우
        answer.append(hap[i])


# print(hap)
# print(fre)
# print(max(fre))
# print(answer)
# print(set(answer))
answer = set(answer)
# answer = list(answer)
# print([i for i in answer ])  # 리스트로 출력하면 안되나??

for i in answer:
    print(i, end =' ')