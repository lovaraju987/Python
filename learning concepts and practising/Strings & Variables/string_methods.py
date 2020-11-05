''' String Methods'''

str1 = 'geeksforgeeks is for geeks'
str2 = 'geeks'

#find()
print(str1.find(str2,2)) # It searches the given string where it is found in another string from starting index

#rfind()
print((str1.rfind(str2,0))) # It also searches the given string where it is found in another string. but it runs the position of the last acccurance

#startswith()
print(str1.startswith(str2)) # It returns true if "str1" starts with "str2" otherwise it returns false

#endswith()
print(str1.endswith(str2)) # It returns true if "str1" ends with "str2" otherwise it returns false

#islower()
print(str1.islower()) # It returns true if all the letters in the string is in lowercase, otherwise it returns false

#isupper()
print(str1.isupper()) # It returns true if all the letters in the string is in uppercase, otherwise it returns false

#lower()
print(str1.lower()) # It converts all the letters in the string to the lowercase.

#upper()
print(str1.upper()) # It converts all the letters in the string to uppercase

#swapcase()
print(str1.swapcase()) # It converts the each letter in the string to the their opposite case.

#title()
print(str1.title()) # It converts the first letter of every word in the string to the capital and remaining letters converts to the small letters

#len()
print(len(str1)) # It returns the length of the string
print(str1.__len__()) # this method also returns the length of the string

#count()
print(str1.count(str2)) #It counts the given string presents number of times. we can also give starting index and ending index like "str1.count(str2,2,14)"

#center()
print(str1.center(35,'x')) #It surrounded the string with given character(allows only one character) upto the given length

#ljust()
print(str1.ljust(35,'x')) # It returns the original string leftside and given character(allows only one character) right side upto the given length of the string

#rjust()
print(str1.rjust(35,'x')) # It returns the original string rightside and given character(allows only one character) left side upto the givne length of the string

#isalpha()
print(str1.isalpha()) # It returns true if all the characters of the string is only alphabets, otherwise returns false

#isalnum()
print(str1.isalnum()) # It returns true if all the characters of the string is combination of numbers and/or alphabets(without any special characters or spaces), otherwise returns false

x = '  '
#isspcace()
print(x.isspace()) # It returns true if the string contains only spaces, otherwise returns false

str3 = ['raju','rani','ramudu','sita']
str4 = '_~'
#join()
print(str4.join(str3)) #This method converts list of strings into onestring with join a given string

str5 = '.....Lova..raju.......'
#strip()
print(str5.strip('.')) # this method is used to delete all the leading and trailing characters mentioned in its arguments

#lstrip()
print(str5.lstrip('.')) # this method is used to delete all the leading characters mentioned in its arguments

#rstrip()
print(str5.rstrip('.')) # this method is used to delete all the trailing characters mentioned in its arguments

#min()
print(min(str1)) # this method returns minimum value alphabet from string

#max()
print(max(str1)) # this method returns maximum value alphabet from string

#replace()
print(str1.replace('geeks','nerds',2)) # the replace() method is used to replace the substring with a new substring in the string. we can set the replace limit also like this by entering the third argument

str6 = 'lova\traju\tpython\tprogrammer'
#expandtabs()
print(str6.expandtabs()) # It is used to replace all tab characters(“\t”) with whitespace. we can set tabsize also like this "str6.expandtabs(6)"

#split()
print(list(str1.split(' '))) #it converts the string into list based on using given substring argument

