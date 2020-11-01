'''
example project, showing a program that analyzes
a sample file to find what percentage of the text
each character occupies. 
'''

file = input('Enter file name:') #taking file name
with open(file,'w') as f:  #writing content
    f.write('''using your web browser program (hopefully Netscape or Mosaic, since these
    are the most commmon brwosers used on the Web), open the
    new file you just saved. It will be formatted just as it will look
    when viewed with that browser program by anyone on the
    Web. If the graphics files you\'ve specified are in the same disk
    directory, they\'ll also appear. Check for mistakes in spacing, spelling,
    and so on to make sure the page looks exactly the way
    you want it to look. If it doesn\'t, make the appropriate changes
    in the text file version of the page using your word processor.''')

with open(file,'r') as g: #reading file content and storing
    text = g.read() 

def count_variable(text,char): #counting given character
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

for char in 'abcdefghijklmnopqrstuvwxyz': #calculating percentage of each given character
    perc = 100 * count_variable(text,char)/len(text)
   # print(char,'=',round(perc,2),'%')
    print('{} = {}%'.format(char,round(perc,2)))