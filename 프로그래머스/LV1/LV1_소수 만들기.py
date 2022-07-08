def solution(nums):
    answer = 0
    
    from itertools import combinations
    x = []
    for i in combinations(nums,3):
        x.append(sum(i))
    
    
    for i in x:
        cnt = 0 
        
        for j in range(1,i + 1):
            if i % j == 0 :
                cnt += 1
        if cnt == 2 :
            answer +=1  
    return answer
    # 다른 사람 풀이
    