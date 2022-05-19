
# 1차 정확성은 100% 인데  효율성이 0%임 그도 그럴게 굳이 저렇게 풀 필요가 없음.
def solution(participant, completion):
    answer = ''
    from collections import Counter
    for i in participant:
        if i not in completion:
            answer = i
    
    if answer =='':
        # 값을 키 : 값으로 뽑고 
        p = dict(Counter(participant))
        c = dict(Counter(completion))

        # 정렬하고 값이 다른 키를 answer로 만든다
        p = sorted(p.items())
        c = sorted(c.items())
        print(p)
        print(c)
        for i in range(len(p)):
            if p[i] != c[i]:
                answer=p[i][0]
    return answer




# 2차 
# Counter끼리 - 연산이 가능한줄 몰랐다..
def solution(participant, completion):
    answer = ''
    from collections import Counter
    
    # 값을 키 : 값으로 뽑고 
    p = Counter(participant)
    c = Counter(completion)
    

    answer = list((p-c).keys())[0]
    return answer


# 다른 사람들 풀이

# Sort/Loop 풀 수도 있음  
def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    # 전부 돌아도 없는 경우
    return participant[len(participant)-1]


    