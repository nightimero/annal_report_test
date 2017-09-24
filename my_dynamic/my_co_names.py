# tuple of names of local variables
# However in practice it appears that co_names is a tuple of global variable names
# while co_varnames is a tuple of local variable names (and argument names). For example:

a = 1

def f(b):
    c = a + b

print(f.__code__.co_varnames)  # prints ('b', 'c')
print(f.__code__.co_names)     # prints ('a',)