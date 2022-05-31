

# III 1057번_토너먼트


# print(1//2)
n,kim,im = map(int,input().split())

cnt = 0
while kim !=im:

    kim = kim - kim//2
    im = im - im//2

    cnt+=1
print(cnt)