class stack:
   s=[]
   def push(self):
      elt=input('Enter A Element in Stack :')
      stack.s.append(elt)
   def display(self):
      l=len(stack.s)
      for i in range(0,l):
         print stack.s[-1-i]

print'                          MAIN MENU FOR STACK'
print'                       *************************'
print'                               1.Push'
print'                               2.pop'
print'                               3.Display'

obj=stack()
c='y'
while c=='y':
   
   ch=input('Enter Your Choice        :')
   if ch==1:
      obj.push()
      print'___________________________________________________________________'

   elif ch==2:
      if obj.s==[]:
         print'Stack is Empty'
         print'________________________________________________________________'
      else:
         print'The Pop Element is',obj.s.pop()
         print'________________________________________________________________'
   elif ch==3:
      print'Status Of The Stack IS'
      obj.display()
      print'___________________________________________________________________'

   c=raw_input('Do You Want To Continue y/n')
