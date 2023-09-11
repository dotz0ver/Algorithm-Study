import sys
input = sys.stdin.readline

A, B, C = list(map(int, input().split()))

def dac(A, B, C):
    if B == 1:
        return A % C
    else:
        num = dac(A, B // 2, C)
        if B % 2 == 0:
            return num * num % C
        else:
            return num * num * A % C

print(dac(A, B, C))