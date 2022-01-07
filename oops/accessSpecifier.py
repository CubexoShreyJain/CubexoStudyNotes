class A:
    var1 = 324                     # Public
    _var2 = 'asdf'                 # Protected
    __var3 =  2345345              # Private
    def print_functionA(self):
        print("var1: {}, var2: {}, var3: {}".format(self.var1, self._var2, self.__var3))

    
class B(A):
    
    def print_function(self): 
        print("var1: {}, _var2: {}".format(self.var1, self._var2))       #Private passes here also, can't print here 

a = A()
print("var1: {}, _var2: {}".format(a.var1, a._var2))             #Private Pass
a.print_functionA()                                              #Access all
b = B()
print("var1: {}, _var2: {}".format(b.var1, b._var2))
a.print_functionA()                                              #Accessed all
b.print_function()                                               #can't access private

print(a._A__var3)                                                #Its the mangled name, now can access var3