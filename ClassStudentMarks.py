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
        print'                          Report Card'
        print'--------------------------------------------------------------------------------'
        print'        Name :',self.Sname,'               RollNumber:',self.Snumber
        print'        Class:XII','                  School:BVM'
        print'-------------------------------------------------------------------------------'
        print'|SUBJECTS','                  MARKS              '
        print'------------------------------------------------------------------------------'
        print "|ENGLISH                    " ,self.english,'              '
        print'------------------------------------------------------------------------------'
        print "|CS                         " ,self.cs,'               '
        print'------------------------------------------------------------------------------'
        print "|MATHS                      ",self.maths,'              '
        print'------------------------------------------------------------------------------'
        print "|PHYSICS                    ",self.physics,'              '
        print'------------------------------------------------------------------------------'
        print "|CHEMISTRY                  ",self.chemistry,'              '
        print'------------------------------------------------------------------------------'
        print "|TOTALMARKS                 ",self.t,'             '
        print'-------------------------------------------------------------------------------'
        print "|PERCENTAGE                 ",self.p,'            '                    
        print'------------------------------------------------------------------------------'
ch=input("Enter the number of students to represent the result:")
n=[] 
for i in range(ch):
    obj=marksheet()
    n.append(obj.Input())

s=input('Enter Snumber To display                            :')
if s==obj.Snumber:
    obj.show()
    


##while n<=ch:
##    obj=marksheet()
##    obj.Input()
##  
##    n+=1
##    s=input('Enter snumber to display')
##    obj.show()
