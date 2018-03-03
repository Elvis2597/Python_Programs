x=raw_input('Enter string')
t=()
a=x.split()
for i in a:
    if i[0]=='a':
        t=t+(i,)
print t
        
