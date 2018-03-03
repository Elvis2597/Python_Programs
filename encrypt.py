def encrypt(x):
    y=len(x)
    a=0
    b=1
    q=j=r=" "
    while a<y:
        q=q+x[a]
        a=a+2,
    while b<=y:
        r=r+x[b]
        b=b+2
        j=q+r
    print q+r
    return j 

def decrypt(x):
    y=len(x)
    if y%2==0:
        a=y/2
        b=y/2
    else:
        a=((y-1)/2)+1
        b=((y-1)/2)
    e=x[:a]
    o=x[(-b):]
    c=1

    d=" "
    count=0
    while c<a:
        d=d+e[count]+o[count]
        count+=1
        c+=1
        if (y/2)==0:
            print d
        else:
            d=d+e[-1]+o[-1]
            print d,
j=raw_input('e')

a=decrypt(j)
b=encrypt(j)

