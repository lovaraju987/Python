# Regex - regex is a seqence of characters that forms a search pattern.
# regex can be used to check if a strinig contains the specified search pattern
# python has a built in package called re, which can be used to work with regular expressions.
# Import the 're' module.



# ''' Fuctions of regular expressions '''
# '''
# The re module offers a set of functions that allows us to search a string for a match:
# 1) Match() - this method matches the regex pattern in the string in first position.
# 2) Search() - this method returns the match object if there is a match found in any position in the string
# 3) findall() - it returns a list that contains all the matches of a pattern in the string.
# 4) split() - returns a list in which the string has been split in each match.
# 5) sub() - replace one or many matches in the string
# '''


# # Metacharacters
# '''
# Metacharacters are characters with a special meaning
# characters      example             explanation
# []              "[a- m]"  -  A set of characters
# \               "\d"      -  signals a special sequence(can also be used to escape special characters)
# .               "he..o"   -  Any character(except newline character)
# ^               "^hello"  -  starts with
# $               "hello$"  -  Ends with
# *               "aix*"    -  Zero or more occurrences
# +               "aix+"    -  one or more occurrences
# {}              "al{2}"   -  Exactly the specified number of occurrences
# |               "fs|ys"   -  Either or 
# ()              "(hello)"  -  capture and group  
# ?               ".?hello"  -  zero and one
# '''


# # Special Sequences
# '''
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# Character	Example	             Description
# \A	       "\AThe"         Returns a match if the specified characters are at the beginning of the string		
# \b	       r"\bain"        Returns a match where the specified characters are at the beginning or at the end of a word
#            r"ain\b"        (the "r" in the beginning is making sure that the string is being treated as a "raw string")	                    	
# \B	       r"\Bain"        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#            r"ain\B"        (the "r" in the beginning is making sure that the string is being treated as a "raw string")	                   	
# \d	       "\d"            Returns a match where the string contains digits (numbers from 0-9)		
# \D	       "\D"            Returns a match where the string DOES NOT contain digits		
# \s	       "\s"            Returns a match where the string contains a white space character		
# \S	       "\S"            Returns a match where the string DOES NOT contain a white space character		
# \w	       "\w"            Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)		
# \W	       "\W"            Returns a match where the string DOES NOT contain any word characters		
# \Z	       "Spain\Z"       Returns a match if the specified characters are at the end of the string	
# '''


# # Sets
# '''
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
# Set	                Description	
# [arn]	        Returns a match where one of the specified characters (a, r, or n) are present	
# [a-n]	        Returns a match for any lower case character, alphabetically between a and n	
# [^arn]         	Returns a match for any character EXCEPT a, r, and n	
# [0123]        	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	        Returns a match for any digit between 0 and 9	
# [0-5][0-9]	    Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	    Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	            In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
# '''

# import re

# data  =   '''Born and raised in a Hindu family in coastal Gujarat,
#            western India, Gandhi trained in law at the Inner Temple,
#            London, and was called to the bar at age 22 in June 4, 1891.
#            After two uncertain years in India, where he was unable 1891 4, June
#            to start a successful law practice, he moved to
#            South Africa in 1893 to represent an Indian merchant in
#            a lawsuit. He went on to stay for 21 years. It was in
#            South Africa that Gandhi raised a family, and first
#            employed nonviolent resistance in a campaign for civil
#            rights. In 1915, aged 45, he returned to India. He set
#            about organising peasants, farmers, and urban labourers
#            to protest against excessive land-tax and discrimination.
#            Assuming leadership of the Indian National Congress in 1921,
#            Gandhi led nationwide campaigns for easing poverty,
#            expanding women's rights, building religious and ethnic amity,
#            ending untouchability, and above all for achieving Swaraj or
#            self-rule.[9
# '''

# reg = r'([A-Za-z]{4}) (\d\d?,) (\d{4})|(1891 4, June)'

# match = re.search(reg, data)

# print(match)

# # if match:
# #     print('group  ',match.group())
# #     print('group 0 ',match.group(0))
# #     print('group 1 ',match.group(1))
# #     print('group 2 ',match.group(2))
# #     print('group 3 ',match.group(3))
# # else:
# #     print('No Match')








