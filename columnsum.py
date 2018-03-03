def enter():
    x=[[input('Enter a Value') for j in range(n)]for i in range(m)]

    return x
def display(x):
    for i in range(m):
        for j in range(n):
            print x[i][j],
        print
def matrix(x):
    for i in range(m):
        Sum=0
        for j in range(n):
            Sum+=x[i][j]
        print Sum



        
m=input('enter raow')
n=input('enter column')
a=enter()
display(a)
matrix(a)
