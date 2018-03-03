class student_record:
    def studata(self):
        self.name=raw_input("Enter Student's Name\t        :")
        self.rollno=input("Enter Student's Roll Number\t:")
        self.percent=input("Enter Student's Percentage\t:")
##    def sort(self,x):
##        for i in range(len(x)-1):
##            small=x[i]
##            position=i
##            for j in range(i+1,len(x)):
##                if small>x[j]:
##                    small=x[j]
##                    position=j
##                    x[i],x[position]=x[position],x[i]
##        return x
    def show(self,l,l1):
        print"-----------------------------------RESULT--------------------------------------"
        print"\t\tNAME\tROLL NO.  PERCENTAGE"
        for j in l1:
            for d in l:
                if j==d.percent:
                    print"________________________________________________________________________________"
                    print"\t\t",d.name,"\t",d.rollno,"\t ",d.percent
                    
n=input("Enter Number of student         :")
l=[]
l1=[]
for k in range(n):
    print
    print"                  For student",k+1
    s=student_record()
    s.studata()
    l.append(s)
    l1.append(s.percent)
s1=student_record()
l1.sort()
s1.show(l,l1)
        




    
