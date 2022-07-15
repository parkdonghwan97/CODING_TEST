def solution(sizes):
    
    # 가로 세로 2개의 모서리 중 큰 값을 모두 가로로 두고   작은 값을 모두 세로로 둔다.
    # 가로/세로 중 가장 큰 값으로 만든 사각형의 넓이가 답이 됨.
    
    l = len(sizes)
    w ,h =0,0
    
    for i in range(l):
        sizes[i].sort()
        # print(sizes)
        w = max(w, sizes[i][0])
        h = max(h,sizes[i][1])
    print(w,h)
    
    return w*h