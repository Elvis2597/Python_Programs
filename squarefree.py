from perfect import*
x=input('Enter a Number :')
l1=[]
for i in range(1,x+1):
    if x%i==0:
        l1.append(i)


for j in l1:
    a=perfect(j)
    
    if a==1:
        j=1
        break
    elif a==0:
        j=0
if j==0:
    print 'The Number is Square Free'
else:
    print 'The Number is Not Square'

    
        
