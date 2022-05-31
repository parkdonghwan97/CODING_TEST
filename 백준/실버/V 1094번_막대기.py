

# V 1094번_막대기


x = int(input())
cnt = 0 
while x !=0 : 
    if x %2 ==1:
        cnt+=1
    x = x//2
print(cnt)



# x = int(input())
# cnt = 0 
# n = 64 
# while x > 0:
#     if n > x :
#         n = n //2
#     else:
#         cnt+=1
#         x -=n 
# print(cnt)



# 다른 사람 풀이 
# 이것도 생각보다 괜찮다. 어짜피 x가 64로 고정되어있으니
# 반씩 나누는 값들을 리스트에 넣고 푸는 방법도 괜찮을 듯

# x = int(input())

# bar = [64,32,16,8,4,2,1]
# cnt = 0

# for i in range(len(bar)):
#     if x== 0 :
#         break
    
#     if x >=bar[i]:
#         cnt += 1
#         x = x-bar[i]
# print(cnt)
    