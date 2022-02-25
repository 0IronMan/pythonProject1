class A:
    def demo(self):
        print("class A demo")

class B(A) :
    def demo(self):
        print("class B demo")
        super().demo()

class C(B):
    def demo(self):
        print("class c demo")
        super().demo()

class parent:
    def demo(self):
        print("class child1, demo")
        super().demo()

class spam(parent):
    def demo(self):
        print("class child2 demo")
        super().demo()

class spam(parent):
    de



class BankAccount:
    intrest = 0.04
    def __init__(self,name,balance):
        self.name = name
        self.blance = blance

    def deposite(self, amount):