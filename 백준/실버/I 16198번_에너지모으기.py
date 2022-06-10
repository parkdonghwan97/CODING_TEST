


# I 16198번_에너지모으기

# 백트래킹 -> 구슬 하나 없애고 양 옆의 수를 곱해서 더함
def dfs(tmp):
    global ans
    if len(a) == 2:
        if ans < tmp:
            ans = tmp
        return
    else:
        for i in range(1, len(a) - 1):
            k = a[i]
            del a[i]
            dfs(tmp + a[i - 1] * a[i])
            a.insert(i, k)


N, a = int(input()), list(map(int, input().split()))
ans = 0
dfs(0)
print(ans)






# 다른사람 풀이
# n = int(input())


# a = list(map(int,input().split()))
# answer = 0 

# def DFS(x,tot):

#     global answer 
#     if len(x)==2:
#         answer = max(answer,tot)
#         return 
#     for i in range(1, len(x)-1):
#         DFS(x[:i] +x[i+1:],   tot+ (x[i-1]*x[i+1])  )


# DFS(a,answer)
# print(answer)