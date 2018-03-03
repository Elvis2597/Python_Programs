print'                          MAIN MENU of Queue'
print'                        **********************'
print'                               1.Insertion'
print'                               2.Deletion'
print'                               3.Display'
l1=[]
ch='y'
while ch=='y':
   ch1=input('Enter Your choice')
   if ch1==1:
      elt=input('Enter A Element in queue')
      l1.append(elt)
   elif ch1==2:
      if l1==[]:
         print'queue IS Empty'
      else:
         print'The Deleted Element is', l1[0]
         del l1[0]
   elif ch1==3:
      l=len(l1)
      for i in range(0,l):
         print i
   print'Wrong Choice'
   ch=raw_input('Do You Want to Continue y/n')
      
