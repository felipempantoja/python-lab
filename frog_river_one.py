#!usr/bin/python

#question: https://codility.com/programmers/lessons/4-counting_elements/frog_river_one/
#my solution: https://codility.com/demo/results/trainingD5GPQ8-AC8/

cases = [
    (2, [2, 2, 2, 2, 2]),
    (5, [1, 3, 1, 4, 2, 3, 5, 4]),
    (3, [1, 3, 1, 3, 2, 1, 3])
]

def solution(case):
    '''my solution. I use a dict to get non-repeated values from the array, and then I keep summing
    these values so I can check if this total sum is equal to the sum of all values from 1 to X.
    Efficient but not much readable'''
    X, A = case
    amap = {}
    total = 0
    for i, a in enumerate(A):
        if a not in amap:
            total += a
        amap[a] = a
        
        if total == (X * (X+1) / 2):
            return i
    return -1

def someones_better_solution(case):
    '''someone s better solution. It s a little more efficient because it has less instructions, 
    but it's far cleaner than mine, because instead of calculate total os sequences, it just gets the size
    of a hashset (no repetitions) and compare with the target position of the leaf'''
    X, A = case
    aset = set()
    for i, a in enumerate(A):
        aset.add(a)
        if len(aset) >= X:
            return i
    return -1

for case in cases:
    print '----------------------'
    print 'case: {}'.format(case)
    print 'result: {}'.format(solution(case))
    print '----------------------'