

# II 1264번_모음의 개수



# while 1:
#     a = 0
#     x = input().lower()

#     if x =='#':
#         break    
#     a += x.count('a')
#     a +=x.count('e')
#     a+=x.count('i')
#     a+=x.count('o')
#     a+=x.count('u')
#     print(a)


    

# 다른 ㅗㅋ드
while True:
    a = input()
    
    if a == '#':
        break
    cnt = 0
    for i in a:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)