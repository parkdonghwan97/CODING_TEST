

# III 1284번_집주소

# 1= 2cm
# 0 = 4cm
# 2 = 3cm
# 숫자 사이 1 cm 
# 왼쪽 오른쪽 1cm 


while 1:
    default= 2 
    n= input()
    
    if n =='0':
        break
    
    # 숫자 사이 값 
    default += len(n)-1

    for i in n:
        if i == '1':
            default +=2
        elif i =='0':
            default+=4
        else:
            default+=3
        
        
    print(default)
