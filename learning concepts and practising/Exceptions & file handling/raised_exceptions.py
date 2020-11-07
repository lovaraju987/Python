''' Raised Exceptions '''

''' using raised exceptions we can rise exceptions manually any where in the program.
to achieve this we used 'raise' keyword 
'''

# print('hi')
# raise ValueError  # we need to specify what type of error we raising

# print(2/2)
# raise ZeroDivisionError('zero division error occured') # we can also print some message with error

try:
    print(3/0)
except:
    print('error occured')
    raise # by this format we can print what type of error eccured without specifying error


