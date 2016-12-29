A = map(int, raw_input().split())
print A
least = None
total = sum(A)
a = 0
for i in xrange(len(A)):
    a += A[i]
    diff = abs(total - a*2)
    if least == None or diff < least:
        least = diff
    if least == 0:
        break
print least