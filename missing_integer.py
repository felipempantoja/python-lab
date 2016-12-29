#!usr/bin/python

#question: https://codility.com/programmers/lessons/4-counting_elements/missing_integer/
#my solution: https://codility.com/demo/results/trainingJUM3XV-SDJ/

cases = [
    [0],
    [-1],
    [-1, 1],
    [-1, 2],
    [1, 3, 5, 7],
    [2, 3],
    [2],
    [1],
    []
]

def solution(A):
    
    A = sorted(A)
    
    if len(A) == 0 or A[-1] < 0: return 1

    amap = {}
    for a in A:
        amap[a] = a
    
    for a in xrange(1, A[-1] + 2):
        if a not in amap:
            return a

for case in cases:
    print '----------------------'
    print 'case: {}'.format(case)
    print 'result: {}'.format(solution(case))
    print '----------------------'