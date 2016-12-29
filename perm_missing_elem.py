A = map(int, raw_input().split())
n = len(A) + 1
print (n * (n + 1) / 2) - sum(A)