''' Generators '''
''''generators used for memory efficient and list-comprehensions is used for execution speed  '''

def countdown(): #generator function
    i=5
    while i > 0:
        yield i
        i-=1
#calling generator using python default generator
print(next(countdown()))
print(next(countdown()))

#calling generator using for-loop
for i in countdown():
    print(f'number is {i}')

#finate generators can be converted into lists
print(list(countdown()))


''' genrators expression vs list-comprehensions :-'''

x = [i*2 for i in range(10)] #list comprehensions
print(x)

print()

y = (i*2 for i in range(10)) #generator expression
print(y) # it returns generator object address only. not printed values. because it is generators
for x in y:
    print(x)






    



