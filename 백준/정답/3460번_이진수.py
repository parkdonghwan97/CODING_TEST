T = int(input())
for _ in range(T):

    n = int(input()) 
    x = bin(n)[2:]

    for i, v in enumerate(x[::-1]):
        if v == '1':
            print(i, end=' ')
    print()        

