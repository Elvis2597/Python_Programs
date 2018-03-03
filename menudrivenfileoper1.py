print'                           MAIN MENU'
print'                       ******************'
print'                       1.To Create a File'
print'                       2.Display'
print'                       3.Reverse Each Word'
print'                       4.To Find Vowel Words'
print'                       5.To Count no. Digits'
print '                      6.To Count Number Of Lines'
ch='y'
while ch=='y':
   ch1=input('enter your Choice')
   if ch1==1:
      
      f=open('test.txt','w+')

      while(1):
         line=raw_input('Enter a Sentence')
         f.write(line)
         choice=raw_input('do you want to add more data y/n')
         if choice.upper()=='N':
            break
   elif ch1==2:
      
      f.seek(0)
      line=f.readlines()
     
      for i in line:
         print i
   elif ch1==3:
      f.seek(0)
      line=f.readlines()
     
      for i in line:
         print i[::-1]

   elif ch1==4:
      f.seek(0)
      line=f.readline()
      x=line.split(' ')
      c=0
      
      for i in x:
         
         if i[0] in 'aieou':
            c+=1
            print i
   elif ch1==5:
      f.seek(0)
      line=f.readline()
      c=0 
      for i in line:
         if i in '0123456789':
            c+=1
      print c
   elif ch1==6:
      c=0
      f.seek(0)
      line=f.readline()
      for i in line:
         if i.strip():
            c-=1
      print c
            
            
      
   

      
   
   
s
