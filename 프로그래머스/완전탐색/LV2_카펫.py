def solution(brown, yellow):
    answer = []
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_x = int(yellow/i)
            yellow_y = i
            # 노랑의 가로 길이*2 + 노랑의 세로길이 *2  +4  = 갈색 격자 수  이걸 어떻게 떠올리지
            if yellow_x * 2 + yellow_y * 2 + 4 == brown:
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                return sorted(answer,reverse=True)









# def solution(brown, yellow):
    # brown + yellow = 총 정사각형 개수 
    # 10 + 2 = 12   4,3
    # 8 + 1 = 9     3,3 
    # 24 + 24 = 48 = 8 6
    
    # 노랑의 가로 길이*2 + 노랑의 세로길이 *2  +4  = 갈색 격자 수  이걸 어떻게 떠올리지
    
#     tot = brown + yellow
    
#     for i in range(3,brown):
#         if tot % i == 0:  
#             j = tot//i
#             if (i-2)*(j-2) ==yellow:
#                 return sorted([i,j],reverse=True)
