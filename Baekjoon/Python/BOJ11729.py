import sys
input = sys.stdin.readline

N = int(input())

def hanoi (N, a, b, c):
    if N == 1:
        print(a, c)
    else:
        hanoi(N-1, a, c, b)
        print(a, c)
        hanoi(N-1, b, a, c)

print(2**N-1)
hanoi(N, 1, 2, 3)