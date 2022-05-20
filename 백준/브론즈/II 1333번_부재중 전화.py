

# II 1333번_부재중 전화

# N 곡 L 길이 D 전화벨   노래와 노래 사이에 1초 

n,l,d = map(int,input().split())

# N * L -> 노래길이    (N-1)*5 조용한 구간   전화벨은D초에 1번씩 울림 1초동안 
bell = 0 
songs = []
for i in range(n):
    for j in range(l):
        songs.append(1)
    for j in range(5):
        songs.append(0) 
while 1:
    if bell >= len(songs):
        break
    if songs[bell] == 0:
        break 
    else:
        bell+=d
print(bell)


# 다른 사람 코드  
    
N ,L, D = map(int, input().split())

t = 0
while t < N * (L + 5):
    if t % (L + 5) >= L:
         break
    t += D
print(t)