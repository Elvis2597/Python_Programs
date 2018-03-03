X=[[input('Enter a Value') for j in range(3)]for i in range(3)]
Y=[[input('Enter the Value') for j in range(3)]for i in range(3)]
result =0

for i in range(len(X)):
   for j in range(len(Y[0])):
      for k in range(len(Y)):
      
          result+= X[i][k] * Y[k][j]

          print result
          break
