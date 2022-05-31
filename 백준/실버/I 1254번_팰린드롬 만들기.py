

# I 1254번_팰린드롬 만들기
#  부분문자열이 팰린드롬이 되기까지의 왼쪽 문자열 개수만큼 더해주면 그게 답이다 
s = input()

for i in range(len(s)):

    # print(s[i])
    # print(s[i:])
    # print(s[i:][::-1])

    if s[i:] == s[i:][::-1]:
        print(len(s)+i)
        break