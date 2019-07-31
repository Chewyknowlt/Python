class A:
    def method(self):
        print('this is class A')

class B:
    def method(self):
        print('This is class B')

class C(A,B):
    pass

obj = C()
obj.method()