def enter():
    x=[[input('Enter a Value') for j in range(n)]for i in range(m)]
    y=[[input('Enter the Value') for j in range(l)]for i in range(b)]
    matrix(x,y)
    return x,y
def matrix(x,y):
    Sum=[[None for j in range(n)]for i in range(m)]
    for i in range(len(x)):
        for j in range(len(y[0])):
            Sum[i][j]=0
            for k in range(len(y)):
                Sum[i][j]+=x[i][k]*y[k][j]
    for r in Sum:
        print r


def angstrong(num):
    Sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       Sum += digit ** 3
       temp //= 10

    if num == Sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")






##m=input('enter raow')
##n=input('enter column')
##l=input('enter raow')
##b=input('enter column')
##a=enter()

p=1
while p<=4:
    ch=input('Enter your choice')
    if ch==1:
        n=input('Enter a number')
        angstrong(n)
    




