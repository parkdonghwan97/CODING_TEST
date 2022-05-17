



for i in range(3):
    answer = 0
    n = int(input())

    for j in range( n ):
        answer += int(input())

    if answer ==0:
        print(0)
    elif answer <0:
        print('-')
    else:
        print('+')
        

