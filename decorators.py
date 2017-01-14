def logger(fn):
    def inner(*args, **kwargs):
        print 'Arguments were: %s and %s' %(args, kwargs)
        return fn(*args, **kwargs)
    return inner



@logger
def add(a, b=1):
    return a + b

@logger
def sub(a, b):
    return a - b

@logger
def foo():
    return 'foo'

def multiply(a, b):
    return a * b


print add(1, 2)
print add(5)
print sub(2, 1)
print foo()

#another way to use decorators in python
multiply = logger(multiply)
print multiply(3, 2)