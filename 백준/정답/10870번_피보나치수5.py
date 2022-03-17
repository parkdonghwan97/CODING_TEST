

n = int(input())
a= [0,1]
for i in range(1,n):
    a.append(a[i]+a[i-1]  )
    #[0, 1]
    #

print(a[n])
