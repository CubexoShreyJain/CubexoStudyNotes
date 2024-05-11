#Yup python too have something called iterators as cpp:
# All the iterable elements(list, tuples, dict, etc.) have 2 methods:
# __iter__ = that returns the first itertor
# __next__ = that moves the iterator to next elements

s = ["hasl", "afd", "afrwed", "gsr"]
it = iter(s) # points to -1
print(next(it)) # now its at index 0
next(it)
print(next(it))

st = "this is a string"
it2 = iter(st)
print(next(it2)) # chars
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

for i in s: #goes through all iterators
    print(i)