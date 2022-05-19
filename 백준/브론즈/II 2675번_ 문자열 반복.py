

# II 2675번_ 문자열 반복


T = int(input())

for i in range(T):
    answer = ''
    R, S = map(str,input().split())
    for j in S:
        print(j*int(R),end='')
    print()
