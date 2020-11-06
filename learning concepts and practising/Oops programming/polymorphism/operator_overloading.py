''' Operator Overloading - magic methods '''

''' operator overloading uses magic methods. magic methods are inbuilt operator methods.
when we performed any operations in program by default these magic methods are executed based on operator we used.'''

'''
normally we can't perform any operations on different objects values each other. 
in this we tried to performing operations on different object values by overriding magic methods.
we need not call the magic methods. they executed automatically when thier operation performed
'''
''' here we practiced some operations only. python has so many magic methods'''

class Student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def __add__(self,other): # different object values
         m1 = self.m1 + other.m1
         m2 = self.m2 + other.m1
         m3 = self.m3 + other.m1
         return Student(m1,m2,m3)
        
    def __sub__(self,other): #subtracting different object values
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        m3 = self.m3 - other.m3
        return Student(m1,m2,m3)
    
    def __str__(self):   # returning the values of the given object
        ''' printing object values some different ways iam tried '''
        subjects = {'maths1':self.m1,'maths2':self.m2,'maths3':self.m3}  # way -1
        for i in subjects:
            print(i,':',subjects[i])
        return 'ended'
        # l = [self.m1,self.m2,self.m3] # way - 2
        # for i, x in enumerate(l,1):
        #     print(f'm{i}:{x}')
        # return 'that\'all'

      #  return f'm1:{self.m1}, m2:{self.m2}, m3{self.m3}' # way - 3
               
        

s1 = Student(10,20,30)
s2 = Student(20,30,40)

sum = s1+s2 # when this time automatically __add__ method called whatever we defined and stored all the values in sum object
print(sum.m1,sum.m2,sum.m3)
print('printing all the results of subjects after added each one')
print(sum)

print()

sub = s1-s2 # when this time automatically __sub__ method called whatever we defined and stored all the values in sub object
print(sub.m1,sub.m2,sub.m3)
print('printiing all the results of subjects after subracted each one')
print(sub)

print()

print('s1 values are :')
print(s1) # printing all the values of s1 object 

print()
print('s2 values are :')
print(s2) # printing all the values of s2 object
