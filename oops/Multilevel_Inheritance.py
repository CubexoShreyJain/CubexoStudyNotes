class A:
    classVar = "class Variable A"
    def __init__(self):
        self.instVar = "instance variable A"
        self.good = "Very VEry good"                     #this would be printed
class B(A):
    classVar = "class Variable B"
    good = "Good froim Calss B"
    def __init__(self): 
        super().__init__()                               # this is important
        self.instVar = "instance variable A"
        # self.good = "VERY GOOD"
class C(B):
    classVar = "class Variable C"
    good = "GOOD"
    def __init__(self):
        super().__init__()
        self.instVar = "instance variable A"
shrey = C()
print(shrey.good)