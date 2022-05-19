

def solution(clothes):
    answer= 0
    d={}
    for i,j in clothes:
        print(i,j)
        if j not in d:
            d[j] = 1
        else:
            d[j]+=1
    answer= 1
    for i in d.values():
        answer *=(i+1)


    return answer-1  # 옷 안입는경우 제외


# [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

# 다른 코드
# 처음에 Counter 쓰다가 막혔는데
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer