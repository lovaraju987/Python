''' Generators '''

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

''' genrators vs list-comprehensions :-
generators used for memory efficient and list-comprehensions is used for execution speed  '''





    



