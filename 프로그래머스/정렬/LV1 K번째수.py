


def solution(array, commands):
    answer = []
    
    for i in commands:
        # print(i)
        # print(array[ i[0]-1 : i[1]  ])
        # print(sorted(array[ i[0]-1 : i[1]  ])[i[2]-1]  )
        answer.append(sorted(array[ i[0]-1 : i[1]  ])[i[2]-1] )
    
    
    
    return answer
    


# 다른사람 코드 
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))