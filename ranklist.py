class marksheet:
    def __init__(self):
        self.Snumber=0
        self.Sname=""
        self.english=23
        self.cs=34
        self.maths=33
        self.physics=16
        self.chemistry=45
    def calc(self):
        self.t=self.chemistry+self.physics+self.cs+self.maths+self.english
        self.p=float((self.t*100)/500)
       
    def Input(self):
        self.Snumber=input("Enter the Snumber of students                       :")
        self.Sname=raw_input("Enter the Sname of students                         :")
        self.english=input("Enter the marks of english                          :")
        self.cs=input("Enter the marks of c-s                              :")
        self.maths=input("Enter the marks of maths                            :")
        self.physics=input("Enter the marks of physics                          :")
        self.chemistry=input("Enter the marks of chemistry                        :")
        self.calculate=obj.calc()
    def show(self):
        print'Name','             Percentage'
        print self.Sname,         self.p
n=[]
ch=input('Enter the Number Of Students                        :')
for i in range(ch):
    obj=marksheet()
    obj.Input()
    n.append(marksheet(obj.show())
             

    
def insertion(l1):
             
             for i in range(1,len(l1)):
              temp=l1[i]
              ptr=i-1
              while ptr>=0 and l1[ptr]>temp:
                 l1[ptr+1]=l1[ptr]
                 ptr-=1
                 l1[ptr+1]=temp
                 for i in l1:
                   print i

insertion(n)
##while n<=ch:
##    obj=marksheet()
##    obj.Input()
##  
##    n+=1
##    s=input('Enter snumber to display')
##    obj.show()
