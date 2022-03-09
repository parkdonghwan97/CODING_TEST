from ntpath import join
import sys
# import sys
# sys.stdin=open("input.txt", "r")
# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 


# 도 : A 
# 개 : B 
# 걸 : c
# 윷 : D
# 모 : E
# 등 1 배 0 
for _ in range(0,3):
    a = list(map(int,input().split()))
    
    if sum(a) == 1 : # 등 1 걸
        print("C")
    elif sum(a) ==2: #  등 2 개
        print("B")
    elif sum(a) ==3: # 등 3 도
        print("A")
    elif sum(a) ==4: # 등 4 모
        print("E")
    else:
        print("D")


