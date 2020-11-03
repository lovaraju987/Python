''' decorators '''
''' decorators of extensions of functions. i.e.. funtions can modifying the another functions is known as decorators '''

def hello():  #first function
    print('Hello World')  

def ext(fun):  #extensiion function
    def fun2():
        print('##############')
        fun()
        print('##############')
    return fun2


#calling extension function - method-1
x = ext(hello)
x()    

#calling extension function - method-2 using @function_name symbol
#and also a single function can have multiple decorators like this.
@ext
def hello2():
    print('hellow world 2')
hello2()