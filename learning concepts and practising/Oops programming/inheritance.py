''' Inheritance '''
'''
inheritance is four types.
1) single-level inheritance - 
2) multilevel inheritance
3) multiple inheritance
4) heirarchy inheritance
'''

'''
super() method - It is used to access super class method from sub class class method
'''

# Single-level inheritance
class A:
    def a(self):
        print('A')

class B(A):
    def b(self):
        print('B')

b = B()
b.a()
b.b()

# Multilevel Inheritance
class C:
    def c(self):
        print('C')

class D(C):
    def d(self):
        print('D')

class E(D):
    def e(self):
        print('E')

e = E()
e.c()
e.d()
e.e()

# Mulitple Inheritance
class F:
    def f(self):
        print('F')

class G:
    def g(self):
        print('G')

class H(F,G):
    def h(self):
        print('H')

h = H()
h.f()
h.g()
h.h()

# Hierarchy Inheritance
class I:
    def i(self):
        print('I')

class J(I):
    def j(self):
        print('J')

class K(I):
    def k(self):
        print('K')

j = J()
j.i()
j.j()
k = K()
k.i()
k.k()

