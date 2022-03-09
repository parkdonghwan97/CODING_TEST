# import sys  
# sys.stdin=open("input.txt","rt")


T = int(input())

for i in range(T):
    anlist =[]
    n,s,e,k = map(int,input().split())

    X = list(map(int,input().split()))
    
    for j in range(0,len(X)):
        if j >= s-1 and j <= e-1:
            anlist.append(X[j])
            anlist.sort()

    print("#",i+1," ",  anlist[k-1],sep="")

    
    
    



