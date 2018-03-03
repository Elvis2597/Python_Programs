##string='CBSEONLINE'
##import random
##number=random.randint(0,3)
##n=9
##while string[n]!='L':
##    print string[n]+string[number]+'#'
##    number=number+1
##    n=n-1
##class traveller:
##    pnr=0
##    def book(self,p):
##        traveller.pnr=p
##        traveller.pnr+=1
##    def __del__(self):
##        print 'Booking Closed'
##def myfun():
##    t=traveller()
##    print t.pnr
##    del t
##
##myfun()
month={31:'jan',51:'feb'}
for i in month:
    print month[i]
month[29]='leapyear'
print month.items()
