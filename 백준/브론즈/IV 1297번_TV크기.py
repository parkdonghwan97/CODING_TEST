

# IV 1297번_TV크기
# import math
# # 대각선, 높이비율 , 너비비율  
# D,H,W = map(int,input().split())

# # 16: 9 
# tmp = D / (H+W)
# DD = D **2

# op = DD/ (H**2 + W**2)

# m = math.sqrt(op)


# # 출력
# # 높이 너비

# # 내림모듈 floor
# print( math.floor(m * H)  , math.floor(m*W))

# # 다른사람 코드   
d,a,b=map(int,input().split())
r = ((d**2)/((a**2+b**2)))**0.5
print(int(r*a), int(r*b))

