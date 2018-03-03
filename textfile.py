print'                           MAIN MENU'
print'                       ******************'
print'                       1.To Create a File'
print'                       2.Display'
print'                       3.Copying a File'
print'                       4.To delete word from File'
print'                       5.Updating a File'
ch='y'
while ch=='y':
   ch1=input('Enter your Choice                :')
   if ch1==1:
      
      f=open('fab.txt','w+')

      while(1):
         line=raw_input('Enter a Sentence                 :')
         f.write(line)
         choice=raw_input('Do you want to add more data y/n :')
         print'________________________________________________________________________________'

         if choice.upper()=='N':
            break
##   elif ch1==2:
##      
##      f.seek(0)
##      line=f.readlines()
##     
##      for i in line:
##         print i
##      print'________________________________________________________________________________'
##   elif ch1==3:
##       f1=open('fab.txt','r')
##       f2=open('hat.txt','w')
##       for i in f1:
##           f2.write(i)
   elif ch1==4:
      
      import os
      f1=open("fab.txt","r")
      f2=open("set.det","w")
      x=f1.readlines()
      word=raw_input('Enter a Word To be Deleted')
      for i in f1:
         
         
         if i!=word:
            f2.write(i)
      f1.close()
      f2.close()
      os.remove('fab.txt')
      os.rename('set.detz','fab.txt')
              
           
       
        
