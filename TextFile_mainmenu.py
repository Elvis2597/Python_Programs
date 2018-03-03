+def create():
    n=raw_input("Enter the name of the file to be created  :")
    f=open((n+".txt"),'w+')
    no=input("Enter number of line\t\t          :")
    for i in range(no):
        line=raw_input("Enter sentence\t\t                 : ")
        f.write(line+"\n")
def show():
    n=raw_input("Enter the name of the file to show\t   :")
    f=open((n+".txt"),'r')
    print f.read()
    f.close()
def copy():
    n1=raw_input("Enter name of the file 1\t\t   :")
    n2=raw_input("Enter name of the file 2\t\t   :")
    f1=open((n1+".txt"),'r')
    f2=open((n2+".txt"),'w')
    lines=f1.read()
    f2.write(lines)
    f1.close()
    f2.close()
def delete():
    n=raw_input("Enter the name of the file\t\t  :")
    x=raw_input("Enter the word to be deleted \t          :")
    temp=open("temp.txt",'w+')
    f=open((n+".txt"),'r+')
    k=f.readlines()
    for i in k:
        j=i.split()
        for q in j:
            if q!=x:
                q=str(q)
                
                temp.write(q+" ")
        temp.write("\n")
    temp.seek(0)
    f.write(temp.read())
    temp.close()
    f.close()
def update():
    n=raw_input("Enter the name of the file                :")
    f=open((n+".txt"),'a+')
    no_up=input("Enter number of line to enter  \t          :")
    for i  in range(no_up):
        line=raw_input("Enter sentence \t\t\t          :")
        f.write(line+"\n")
b=1
while b==1:
    print "                                Main Menu"
    print'                       *****************************'
    print"                             1.CREATE FILE"
    print"                             2.SHOW FILE"
    print"                             3.COPY FILE"
    print"                             4.DELETE FILE DATA"
    print"                             5.UPDATE FILE"
    print"\n"
    ch=input("ENTER YOUR OPTION\t\t          :")
    print""
    if ch==1:
        print"           CREATE A FILE"
        create()
    if ch==2:
        print"\tSHOW FILE"
        show()
    if ch==3:
        print"\tCOPY FILE DATA"
        copy()
    if ch==4:
        print"\tDELETE FILE DATA"
        delete()
    if ch==5:
        print"\tUPDATE FILE"
        update()
    cont=raw_input("DO YOU WANT TO CONTINUE \t          :")
    print
    if cont.upper()=="N":
        b=2
        print "\tTHANK YOU"
        
        
        
