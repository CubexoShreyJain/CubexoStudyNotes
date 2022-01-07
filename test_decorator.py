def dec(func):
    print (" In outter function")
    def new_func():                               
        print (" In inner function")
        func()
    return  "Shrey"

@dec                                           # Test shows that A decorator only takes a function as an argument but can convert
def test_func():                               # function below to any dataType 
    print("Hello Shrey")

print(type(test_func))