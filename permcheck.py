#question: https://codility.com/programmers/lessons/4-counting_elements/perm_check/
#my solution: https://codility.com/demo/results/trainingAWFGY9-3XD/

def solution(A):
    a = set(A)
    len_elements = len(a)
    if len(A) != len_elements: return 0
    sum_elements = len_elements * (len_elements+1) / 2
    return 1 if sum(a) == sum_elements else 0

print solution(map(int, raw_input().split()))