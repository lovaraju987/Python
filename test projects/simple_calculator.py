'''
Write a program to take two integers as input and output their sum/sub/mul/div by the user requirement.

Sample Input:
2
8

Sample Output:
sum is 10
'''
#taking input from user
x = int(input('enter x value:'))
y = int(input('enter y value:'))

#displaying options to the user
options = {1:'sum',2:'sub',3:'mul',4:'div'}
for i in options:
    print(i,':',options[i])

#taking option from the user
op_value = int(input('Enter an option number given to perform that operation:'))

#performing operation by using normal if-else method
# if op_value == 1:
#     print('sum of x and y is ',x+y)
# elif op_value ==2:
#     print('difference of x and y is ',x-y)
# elif op_value ==3:
#     print('product of x and y is ',x*y)
# elif op_value ==4:
#     print('division of x and y is ',x/y)
# else:
#     print('Invalid Option')

# performing operation by using Short if-else hand method
print('sum of x and y is ',x+y) if op_value == 1 else print('difference of x and y is ',x-y) if op_value ==2 else print('product of x and y is ',x*y) if op_value ==3 else print('division of x and y is ',x/y) if op_value ==4 else print('Invalid Opiton')

