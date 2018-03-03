def Armstrong(num):
    Sum = 0

# find the sum of the cube of each digit
    temp = num
    while temp > 0:
       digit = temp % 10
       Sum += digit ** 3
       temp //= 10

# display the result
    if num == Sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")


n=input('Enter a Number')
angstrong(n)
