class A:
    def __init__(self,a):
        self.a=a
class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b=b
class C(A):
    def __init__(self, a,c):
        super().__init__(a)
        self.c=c
class D(B,C):
    def __init__(self, b,a,c):
        B.__init__(self, a, b)
        C.__init__(self, a, c)
d =D(1,2,3)
#no entendemos porque no funciona y hemos probado varias cosas