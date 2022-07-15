from itertools import permutations

# 소수 판별 함수
def isPrinme(x):
    if x < 2:
        return 0
    for i in range(2,x):
        if x%i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    tmp = []
    s = set()
    for i in range(1,len(numbers)+1):
        # 순열이용해 모든 조합을 set을 사용해 중복 제거하고 join, map을 사용해 묶음
        for j in (permutations(numbers,i)):
            s.add(int(''.join(j)))
    print(s)
    
    for i in s:
        if isPrinme(i) == 1:
            answer+=1
        
            
    
    
    
    
    return answer 
    
    