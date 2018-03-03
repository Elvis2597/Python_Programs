def selectionsort():
   l1=input('Enter list')
   small=l1[0]
   for i in range(0,len(l1)):
      small=l1[i]
      pos=i
      for j in range(i,len(l1)):
         if l1[j]<small:
            small=l1[j]
            pos=j
         j+=1
      temp=l1[i]
      l1[i]=small
      l1[pos]=temp
      print'Pass',i+1,':', l1

def bubble():
   l1=input('Enter a List')
   for i in range(0,len(l1)):
      for j in range(0,len(l1)-1-i):
         if l1[j]>l1[j+1]:
            temp=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=temp
            print'Pass',i,':', l1
def insertion():
   l1=input('Enter a List')
   for i in range(1,len(l1)):
      temp=l1[i]
      ptr=i-1
      while ptr>=0 and l1[ptr]>temp:
         l1[ptr+1]=l1[ptr]
         ptr-=1
      l1[ptr+1]=temp
      print'Pass',i,':', l1


print'                      Main Menu'
print'          1.Sort list using Selection Sort'
print'          2.Sort list Using Bubble Sort'
print'          3.Sort using Insertion sort'
ch='y'
while ch=='y':
   ch1=input('Enter Your Choice :')
   if ch1==1:
      selectionsort()
   if ch1==2:
      bubble()
   if ch1==3:
      insertion()
   if ch1>=4:
      print 'Wrong choice'
   ch=raw_input('Do you Want To Continue y/n :')
   
