import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s = list()
o = list()

for i in range(M):
    a, b = input().split()
    s.append(int(a))
    o.append(int(b))

s = min(s)
o = min(o)

if s < o * 6:
    if s < (N % 6) * o:
        print((N // 6) * s + s)
    else:
        print((N // 6) * s + (N % 6) * o)

elif s >= o * 6:
    print(N * o)