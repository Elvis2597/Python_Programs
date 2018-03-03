def matrix(x):
    for i in range(m):
        for j in range(n):
            if i<=j:
                print x[i][j] ,
        print

def enter():
    x=[[input('Enter a Value') for j in range(n)]for i in range(m)]

    return x


m=input('enter raow')
n=input('enter column')
a=enter()
matrix(a)
