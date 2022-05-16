
a,b = map(str,input().split())

lena=len(a)
lenb=len(b)

answer = 0 
for i in range(lena):
    for j in range(lenb):
        answer += int(a[i])* int(b[j])
print(answer)

