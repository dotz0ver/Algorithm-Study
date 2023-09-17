import sys
input = sys.stdin.readline

pibo = [0 for i in range(101)]
pibo[1] = 1
pibo[2] = 1
pibo[3] = 1

for i in range(4, 101):
    pibo[i] =  pibo[i-3] + pibo[i-2]

T = int(input())
for i in range(T):
    N = int(input())
    print(pibo[N])