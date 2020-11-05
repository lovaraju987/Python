'''  Enumerators '''
''' enumerator() methods add a counter value to the iterable lists, strings or etc..'''

things = ['laptop','mouse','pen','charger','keyboard']

for x in enumerate(things): #using enumerator in loops. In this it automatically assigs counter value to the list. but it displays in brackets
    print(x)

print()

for i,x in enumerate(things): #using enumerator in loops. in this we manually defined counter variable. so that it doesn't print brackets. it prints space between the counter value and list value
    print(i,x)

print()

for i,x in enumerate(things,3): #we can set starting counter value like this. by default enumerator starts counting from 0.
    print(i,x)

print()

print(list(enumerate(things))) #it prints directly into list by combing counter value and list value in touple