

# I 1268번_임시 반장

n = int(input())
stu  = []     # 반 
# 행에 있는 학생이 열에 있는 학생과 같은 반을 한 적이 있는지 여부를 저장한 2차원 리스트
answer = [0] * n 

for i in range(n):
    stu.append(list(map(int,input().split())))
    answer[i] = [0] * n 

for i in range(5):      # i 학년
    for j in range(n):  # j 번의 i 학년
        for k in range( j+1 ,n):  # k번의 i 학년을 비교 

            # j번과 k번이 i 학년때 같은 반인경우 answer를 1로 
            if stu[j][i] == stu[k][i]:
                answer[k][j] = 1 
                answer[j][k]  =1 


cnt = [] 
for i in answer:
    cnt.append(i.count(1))
print(cnt.index(max(cnt))+1)


# 다른 사람 코드 

n = int(input())
nlist = [list(map(int,input().split()))  for i in range(n)]

studnet = [0] * n 

for i in range(n):
    for j in range(n):
        for idx in range(5):
            if i==j :         # 행 열이 같은경우
                break 
            if nlist[i][idx] == nlist[j][idx]:
                studnet[i] +=1
                break 
print(studnet.index(max(studnet)) +1 )