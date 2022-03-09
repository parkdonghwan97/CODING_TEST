#import sys  
#sys.stdin=open("input.txt","rt")


p, k = map(int,input().split())

plist = []

for i in range(1,p+1):
    # print(i)  1 ~ p
    if p % i == 0 :
        plist.append(i)
        
        
if k > len(plist):
    print(-1)
else:
    print(plist[k-1])

