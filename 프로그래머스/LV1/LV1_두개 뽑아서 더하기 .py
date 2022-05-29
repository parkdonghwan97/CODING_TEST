# LV1 두개 뽑아서 더하기 
def solution(numbers):
    answer = []
    from itertools import combinations
    for i in (combinations(numbers,2)):
        answer.append(sum(i))
    x = set(answer)
    return sorted(list(x))

