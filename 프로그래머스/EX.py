# LV1_3진법 뒤집기
# def solution(numbers):

#     a= [0,1,2,3,4,5,6,7,8,9]
#     for i in numbers:
#         if i in a:
#             a.remove(i)

#     return sum(a)
def solution(n):
    answer = ''
    while(n>=1):
        a = n % 3 
        n = n//3
        answer += str(a)
    
    
    return int(answer,3)