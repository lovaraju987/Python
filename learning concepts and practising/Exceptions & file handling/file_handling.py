''' File Handling '''

# # write mode
# f1 = open('testfile.txt','w')

# # read mode
# f2 = open('testfile.txt','r')

# # binary write mode
# f3 = open('testfile.txt','wb')

# # binary read mode
# f4 = open('testfile.txt','rb')

# # 
# f5 = open('testfile.txt','rb')

# # file closing
# f1.close()

# file = open('testfile.txt','r+') # + allows file to perform extra operations also like read and write
# file.write('this is a test file')
# file.close()

file1 = open('testfile.txt','r')
print(file1.read()) # after all contents in a file have been read, any attempts to read further from that file will return an empty string, because we are trying to read from the end of the file
print(file1.read(5)) # reading certain characters in the file from starting
print(file1.read(-2)) # negative values returns all the content in the file
file1.close()

file3 = open('testfile.txt','r+')
print(file3.readlines()) # printing line by line from starting
for x in file3: # printing line by line from starting using for loop
    print(x)
file3.close()



''' good practice to using exceptional handling statements when performing file handling operation '''
try:
    f = open('testfile.txt')
    print(f.read())
finally:
    f.close()

''' An alternative way of doing this is using "with" statements.
This creates a temporary varaible, which is only accessible in the indented block of the "with" statement
'''
with open('testfile.txt') as x: # by this way we need not close the file manually. It closes the automatically at the ending of the with block
    print(x.read()) 