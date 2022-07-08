def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        x = a[i]* b[i] 
        answer += x
    
    
    return answer