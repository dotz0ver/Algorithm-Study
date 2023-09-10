import sys
input = sys.stdin.readline

N = int(input())
info = []

for _ in range(N):
    info.append(list(map(int, input().split())))

info.sort(key=lambda x: (x[1], x[0]))

time = 0
res = 0

for i in info:
    if time <= i[0]:
        time = i[1]
        res += 1

print(res)