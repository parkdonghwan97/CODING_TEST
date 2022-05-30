

# III 1051번_숫자 정사각형   # 직관적인 방법

# 브루트 포스 완전탐색 문제
# 가장큰 정사각형 => 최대 크기부터 해야 시간복잡도에서 안걸릴듯.
# 네 꼭지접 크기 같은 경우 return + break

def sol(x):
    for i in range(n-x+1):
        for j in range(m-x+1):
            # 4개 꼭지점 같을 때
            if numbers[i][j] == numbers[i][j+x-1] ==  numbers[i+x-1][j] ==numbers[i+x-1][j+x-1]:
                return True 
    return False

n,m = map(int,input().split())

numbers = [list(map(int,input()))    for _  in range(n)]

size = min(n,m)

for i in range(size,0,-1):

    if sol(i) : 
        print(i**2)
        break




