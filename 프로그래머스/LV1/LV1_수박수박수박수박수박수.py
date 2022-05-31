# LV1_수박수박수박수박수박수
def solution(n):
    answer = n
    x = ''
    for i in range(answer):
        if i %2 ==0:
            x+="수"
        else:
            x+='박'
    
    print(x)
    
    return x