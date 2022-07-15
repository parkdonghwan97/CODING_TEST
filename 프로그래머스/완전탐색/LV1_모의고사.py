def solution(answers):
    answer = []
    
    a1 = [1,2,3,4,5]       # 5개
    a2 = [2,1,2,3,2,4,2,5] # 8개
    a3 = [3,3,1,1,2,2,4,4,5,5] # 10개
    
    cnt1,cnt2,cnt3 = 0,0,0
    
    
    
    for i in range(len(answers)):
        if answers[i] == a1[ i % 5] :
            cnt1 +=1
        if answers[i] == a2[i%8]:
            cnt2+=1
        if answers[i] ==a3[i%10]:
            cnt3+=1
    print(cnt1,cnt2,cnt3)
    tmp = max(cnt1,cnt2,cnt3)
    if tmp == cnt1:
        answer.append(1)
    if tmp ==cnt2:
        answer.append(2)
    if tmp ==cnt3:
        answer.append(3)
    
    return answer