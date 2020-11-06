''' Exception Handling '''

''' to handle exceptions three statements are there
1) try - it contains code that might throw an exception. if that exception occurs, the code in the try block 
             stops the execution and transfer control to the 'except' block
2) except - if no error occurs, the code in the except block doesn't run
3) finally - if either exception occurs or not occurs, the code in this block is executed definatley
'''

try:
    x = 10
    y = 0
    print(x/y)
# except: # used this type when we don't know which exception can be raised
#     print('exception 1')
# except Exception as x: # used this type when we need to know which exception raised. using the x variable we print the what error occured. not only use x, we can use different varaible. that is our choice
#     print('exception 2',x) 
except ZeroDivisionError:
    print('exception 3 is zero division error occured')
# except (ValueError,TypeError): # used this type when we need to handling multiple errors at a time whatever we expect
#     print('exception 4 is occured')
finally:
    print('final block executed')