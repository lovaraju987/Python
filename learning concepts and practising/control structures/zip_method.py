''' zip method'''

''' 
The zip method iterates the multiple iterable lists, strings etc.
but that data types must be same. like list-list, dic-dict, string-string, etc..
'''

vehicles = ['cycle','bikes','buses','cars','scooties']
electronics = ['laptop','cell','keypad','mouse']
electronics1 = ['laptop','cell','keypad','mouse']



for x,y,z in zip(vehicles,electronics,electronics1): #zipping lists
    print(x,y,z)

a,b,c = zip(*[('cycle','bikes','buses'),
                    ('laptop','cell','keypad'),
                    ('laptop','cell','keypad')])   
                    
print(a)  #unzipping lists. in this length of lists can't be greater than 3
print(b) 
print(c) 