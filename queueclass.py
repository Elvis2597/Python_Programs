class queue:
   q=[]
   def push(self):
      elt=input('Enter A Element in queue :')
      queue.q.append(elt)
   def display(self):
      l=len(queue.q)
      for i in range(0,l):
         print queue.q[i]

print'                          MAIN MENU of Queue'
print'                       *************************'
print'                               1.Insertion'
print'                               2.Deletion'
print'                               3.Display'

obj=queue()
c='y'
while c=='y':
   
   ch=input('Enter Your Choice        :')
   if ch==1:
      obj.push()
      print'________________________________________________________________________________'

   elif ch==2:
      if obj.q==[]:
         print'queue is Empty'
         print'____________________________________________________________________'
      else:
         print obj.q[0]
         del obj.q[0]
         
         print'________________________________________________________________________'
   elif ch==3:
      print'Status Of The queue IS'
      obj.display()
      print'____________________________________________________________________________'

   c=raw_input('Do You Want To Continue y/n')

