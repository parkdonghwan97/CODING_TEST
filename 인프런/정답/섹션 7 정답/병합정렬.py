 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();


# 0412 병합정렬
def Dsort(lt,rt):

    # [23,11,45,36,15,67,33,21]        D(0, 7)    mid = (0+7) //2
    #                              D(0,3)    D(4,7)    mid= (0+3)//2  , (4+7)//2
    #                          D(0,1) D(2,3) D(4,5) D(6,7)
    if lt < rt :
        mid = (lt+rt) //2 
        Dsort(lt,mid)
        Dsort(mid+1,rt) # 두 갈래로 뻗음

        # 왼쪽 
        p1  = lt

        # 오른쪽
        p2 = mid+1
        
        # 왼쪽 오른 쪽 비교 후 저장 할 리스트
        tmp = [] 
        while p1 <= mid and p2 <=rt : 

            if arr[p1] <arr[p2]:
                tmp.append(arr[p1])
                p1 +=1 
            else: # 반대인경우
                tmp.append(arr[p2])
                p2+=1
        if p1 <=mid : 
            tmp= tmp+ arr[p1:mid+1]  # mid까지

        if p2 <=rt:
            tmp = tmp+arr[p2:rt+1]  # rt까지 
        
        for i in range(len(tmp)): # 합한 개수만큼

            arr[lt+i] = tmp[i] #   arr의 i번째값을 바꾸면 안된다.


arr = [23,11,45,36,15,67,33,21]
print("정렬 전 : ",*arr)
Dsort(0,7)  # divide & conquer 분할 정복 # 0 ~ 7번 인덱스 정렬 
print()
print("정렬 후 : ",*arr)

