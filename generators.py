def gen1(n):
    yield n
    yield n + 1

g = gen1(5)
print next(g)
print next(g)

print ''

g = (x**2 for x in range(3))
print next(g)
print next(g)
print next(g)

print ''

g = (x**2 for x in range(3))
for n in g:
    print n

print ''

def fibgen(n):
    a,b = 1,1
    for i in range(n):
        yield a
        a,b = b,a+b

for i in fibgen(5):
    print i
