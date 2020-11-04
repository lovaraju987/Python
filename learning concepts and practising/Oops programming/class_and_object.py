''' class and object'''

class con:
    def config(self):
        x =1
        print(f'it is a first class and object {x}')
        print('it is a first class and object {a}'.format(a=x))

y = con()
y.config()