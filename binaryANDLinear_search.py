def binary(List,val):
   low=0
   high=len(List)
   while low<=high:
      mid=int((low+high)/2)
      if List[mid]==val:
         print'Value Found'
         break
      if List[mid]>val:
         high=mid-1
      if List[mid]<val:
         low=mid+1



def linear():
   l1=input('Enter a List')
   val=input('Enter The to be found')
   c=0
   for i in l1:
      
      c+=1
      if i==val:
         print'Value Found',c-1
         break
         
   else:
      print'Value Not found'



print'                         Main Menu'
print'                      1.Linear Search'
print'                      2.Binary Search'
ch='y'
while ch=='y':
   ch1=input('Enter Your Choice')
   if ch1==2:
      a=input('Enter a List')
      val=input('Enter the value')
      binary(a,val)
   if ch1==1:
      linear()
   ch=raw_input('Do you want to continue y/n')


      
