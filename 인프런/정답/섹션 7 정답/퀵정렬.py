 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();


def Qsort(lt,rt):           #arr [45,21,23,36,15,67,11,60,20,33]   피봇값 기준 작으면 왼쪽 크면 오른쪽
                            # 교환 일어나면 인덱스 1증가 

    if lt < rt :                                    # Q(0,9)
                                                # Q(0,4)  Q(6,9)
        pos = lt  # 정렬하고자하는 지점   분할된 영역의 시작지점.
        pivot = arr[rt]  # pivot은 가장 오른쪽 영역

        for i in range(lt, rt):   
            if arr[i] <= pivot :   # 피봇값까지 작으면 swap 
                arr[i],arr[pos] = arr[pos] ,arr[i]  
                pos += 1     
        arr[rt],arr[pos] = arr[pos] ,arr[rt]  
        # return 
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)
                



arr = [45,21,23,36,15,67,11,60,20,33]
print("정렬 전 : ",*arr)
Qsort(0,9) 
print()
print("정렬 후 : ",*arr)

