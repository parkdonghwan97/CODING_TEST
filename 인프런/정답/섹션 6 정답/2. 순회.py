# import sys
# sys.stdin = open('input.txt')


# 전위 - 부모 왼쪽 오른쪽
# 중위 - 왼쪽 부모 오른쪽
# 후위 - 왼똑 오른쪽 부모 

# 전위 순회
def DFS1(v):          # v는 부모 노드 
    if v > 7  :  
        return   # 7보다 크면 종료

    else :         # 7이하인경우

        print(v,end=' ')   # 부모 노드 
        DFS1(v*2)   # 왼쪽 노드 호출  부모노드 * 2
        DFS1(v*2+1) # 오른쪽 노드     부모노드 * 2 + 1



# 중위 순회 
def DFS2(v):          # v는 부모 노드 
    if v > 7  :  
        return   # 7보다 크면 종료

    else :         # 7이하인경우

          
        DFS2(v*2)   # 왼쪽 노드 호출  부모노드 * 2
        print(v ,end=' ')    # 부모 노드
        DFS2(v*2+1) # 오른쪽 노드     부모노드 * 2 + 1

# 후위 순회 
def DFS3(v):          # v는 부모 노드 
    if v > 7  :  
        return   # 7보다 크면 종료

    else :         # 7이하인경우

             
        DFS3(v*2)   # 왼쪽 노드 호출  부모노드 * 2
        DFS3(v*2+1) # 오른쪽 노드     부모노드 * 2 + 1
        print(v ,end=' ')    # 부모 노드
if __name__ =="__main__":
    DFS1(1)
    print()
    DFS2(1)
    print()
    DFS3(1)