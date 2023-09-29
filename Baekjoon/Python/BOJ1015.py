import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

index = [-1] * N

for i in range(N):
    idx = A.index(min(A))
    index[idx] = i
    A[idx] = 1001
print(' '.join(map(str, index)))