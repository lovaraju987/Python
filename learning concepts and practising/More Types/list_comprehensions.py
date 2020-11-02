''' List comprehensions '''
#syntax of list comprehensions is  [expression for item in list]

string = [char for char in 'Lovaraju']  #converting string to list of characters
print(string)

math = [x*5 for x in [2,3,4,2,5]]  #performing operations with multiple inputs by storing in lists
print(math)

conditions = [y*4 for y in [1,2,3,4,5] if y % 2 == 0] #performing operation using conditions
print(conditions)

nested_conditions = [y*4 for y in [1,2,3,4,5] if y>0 if y % 2 ==0] #performing operations using multiple conditions
print(nested_conditions)

else_conditions = ['even' if y % 2 == 0 else 'odd' if y % 2 != 0 else 'different number' for y in [1,2,3,4,5]] # printing different output based on conditions
print(else_conditions)

matrix = [[1,2],[3,4],[5,6],[7,8],[9,10]]
transpose_of_matrix = [ [row[i] for row in matrix] for i in range(2)] #trnaspose of matrix using nested concepts equals to nested loops
print(transpose_of_matrix)

''' list comprehensions vs for loop '''
''' list comprehensions vs lambda funcitons '''