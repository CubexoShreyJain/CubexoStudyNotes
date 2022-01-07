def dec(func):
    print (" In outter function")
    # def new_func():
    #     print (" In inner function")
    #     func()
    return 

@dec


def test_func():
    print("Hello Shrey")

test_func( )


# test_func = dec(test_func)
# test_func()
# new_func()