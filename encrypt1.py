str1=raw_input('Enter Your String')
for i in range(0,len(str1),2):
    print str1[i],
for j in range(1,len(str1),2):
    print str1[j],
print

str2=raw_input('Enter Your Decrypt String')
n=len(str2)
mid=int(n/2)
for k in range(0,n):
    try:
        print str2[k],str2[k+1+mid],
    except IndexError:
        break
