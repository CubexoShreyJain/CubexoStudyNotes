# lambda arguments: expression
# use when anoumous function required for short period of time also a one liner required

x= lambda x, y: x+y*y
print(x(2, 3))

def func(x):
    return lambda : x*x

w = func(4)
print(w())