def solution(numbers):
    answer = ''
    tmp = [] 
    # strnumbers= list(map(str,numbers))
    from itertools import permutations
    
    for i in permutations(numbers,len(numbers)):
        x = ""
        for j in i:
            x+=str(j)
            
        tmp.append(x)
        tmp = list(map(int,tmp))
        answer = str(max(tmp))
        
    
    return answer


# 음 이거 26.7점이 뜬다.  시간초과라는데 어떻게 해야되지  -> permutation 함수 쓰면 안될듯
'''
x * 3 -> 문자열에 3을 곱해주면 해당문자열을 3개 나열하는 것과 같으니

'333', '303030', '343434', '555', '999'를 key로 넣어주면.

 

정렬을 하면 303030 -> 333 -> 343434 -> 555 -> 999가 될 것인데

reverse=True로 해서 거꾸로 정렬된 결과가 리턴됨.
'''
def solution(numbers):
    answer = ''
    strnumbers = list(map(str,numbers))
    strnumbers.sort(key= lambda x: x*3,   reverse=True)
    # print(strnumbers)
    # for i in strnumbers:
    #     answer = answer+i
    
    return str(int(''.join(strnumbers)))