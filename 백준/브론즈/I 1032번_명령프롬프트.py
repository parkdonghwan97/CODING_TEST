n= int(input())

first = list(input()) 


for i in range(n-1):
    
    file = list(input())

    for j in range(len(first)):
        
        if first[j] != file[j]:
            first[j] = '?'
print("".join(first))