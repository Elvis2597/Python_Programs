print'                           MAIN MENU'
print'                       ******************'
print'                       1.To Create a File'
print'                       2.Display'
print'                       3.Reverse Each Word'
print'                       4.To Count Vowel Words'
print'                       5.To Count no. Digits'
print'                       6.To Count Number Of Lines'
ch='y'
while ch=='y':
   ch1=input('Enter your Choice                :')
   if ch1==1:
      
      f=open('test.txt','w+')

      while(1):
         line=raw_input('Enter a Sentence                 :')
         f.write(line)
         choice=raw_input('Do you want to add more data y/n :')
         print'________________________________________________________________________________'

         if choice.upper()=='N':
            break
   elif ch1==2:
      
      f.seek(0)
      line=f.readlines()
     
      for i in line:
         print i
      print'________________________________________________________________________________'
   elif ch1==3:
      f.seek(0)
      line=f.readline()
      x=line.split()
     
      for i in x:
         print i[::-1],
      print   
      print'________________________________________________________________________________'


   elif ch1==4:
      f.seek(0)
      line=f.readline()
      x=line.split(' ')
      c=0
      
      for i in x:
         
         if i[0] in 'aieou':
            c+=1
            print i
      print c,'Times Vowel Words are present'
      
      print'________________________________________________________________________________'

   elif ch1==5:
      f.seek(0)
      line=f.readline()
      c=0 
      for i in line:
         if i in '0123456789':
            c+=1
      print' Numbers present in file are',c
      print'________________________________________________________________________________'

   elif ch1==6:
      
      f.seek(0)
      line=f.readlines()
      l=len(line)
      print'Number of lines are', l
      print'________________________________________________________________________________'
      break
      
   

      
   
   

