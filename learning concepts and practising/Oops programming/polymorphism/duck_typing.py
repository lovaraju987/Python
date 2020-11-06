''' Duck Typing '''

''' Duck Typing is a featuire Dynamic language. it doesn't mater what type, it give priority for only what they behavior.
we can share one class object into another to use that class features in another withouth using inheritence concept '''

class Student:
    def learning(self):
        print('learning')
    def executing(self):
        print('executing')

class Student1:
    def learning(self):
        print('learning')
    def executing(self):
        print('executing')

class Teacher:
    ''' here teacher class also have some behaviour(methods) of student class. here we shoudn't use again that behaviours. we implementing directly by using thier object. so it reduces code.'''
    def __init__(self,obj): #getting another object of classs and using that data in this class
        obj.learning()
        obj.executing()
    def teaching(self):
        print('Teaching')

''' here student and student1 class has same behaviours(methods). so we using single object to call those behaviours whaterver we need by taking object as argument insteed of calling multiple times with multiple objects '''
def functioning(obj):  # here we didn't know which object of class we using. it is depends on what type which object we passing as argument when this function calling
    obj.learning()
    obj.executing()

s = Student()
s1 = Student1()
t = Teacher(s)
t.teaching()

print()

functioning(s)
functioning(s1)

print()

for obj in Student(),Student1(): # calling similar behaviours of multiple classes at a time using only one object. this is the greatness of ducktyping
    obj.learning()
    obj.executing()
