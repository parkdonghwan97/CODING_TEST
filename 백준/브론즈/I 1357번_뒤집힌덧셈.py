

# I 1357번_뒤집힌덧셈


def Rev(x):
    if len(x)==2:
        tmp1 = x[1]
        tmp2 = x[0]
        newx =  tmp1+tmp2 
        return newx
    elif len(x)==3:
        tmp1=x[2]
        tmp2=x[1]
        tmp3=x[0]
        newx=tmp1+tmp2+tmp3 
        return newx
    elif len(x)==4:
        tmp1=x[3]
        tmp2=x[2]
        tmp3=x[1]
        tmp4=x[0]
        newx=tmp1+tmp2+tmp3 +tmp4
        return newx
    elif len(x)==1:
        return x
    else:
        return 1



a,b = map(str,input().split())

x = int(Rev(a)) + int(Rev(b) )

print(  int(Rev(str(x))) )

## 코드가 너무 더럽다. 다른사람들의 코드를 볼까
print(int(str(sum(map(int,input()[::-1].split())))[::-1]))
#너무 쉽게 푸시네 ㅠ

# 다른 코드 

x, y = input().split()
x = list(x)
y = list(y)

x.reverse()
y.reverse()

x_r = "".join(x)
y_r = "".join(y)

hap = int(x_r) + int(y_r)
hap = list(str(hap))
hap.reverse()
hap_r = "".join(hap)
print(int(hap_r))

## list.reverse()가 있구나
## reverse를하고  "".join()으로 