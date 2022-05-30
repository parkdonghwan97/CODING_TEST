

# IV 11948번_과목선택
a = []
b= []
for i in range(4):
    a.append(int(input()))
a.sort(reverse=True)
for i in range(2):
    b.append(int(input()))
b.sort(reverse=True)

print(a[0]+a[1]+a[2]+b[0])