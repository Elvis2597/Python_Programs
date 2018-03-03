def fibonaccii():
    n=input('Enter a Number >2  :')
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b
        
for i in fibonaccii():
    print i,
