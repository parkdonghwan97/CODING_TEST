

# I 1259번_팰린드롬수



# while True:
#     n = input()
#     if n=='0':
#         break
#     point = len(n)//2 
    
#     if len(n) % 2 == 0 :
  
#         if n[:point] ==n[-1:point-1:-1  ]:
#             print('yes')
#         else:
#             print('no')


#     else:
#         if n[:point] ==n[-1:point:-1]:
#             print('yes')
#         else:
#             print('no')

# 다른사람 코드  우와 이거 홀짝을 나눌 필요가 없었네


while 1:
    n = input()
    if n =='0':
        break

    elif n == n[::-1]:
        print('yes')
    else:
        print('no')