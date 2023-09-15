import sys
input = sys.stdin.readline

N = int(input())
f = [0] * 50
f[1] = f[2] = 1

def fibo(N):
    for i in range(3, N+1):
        f[i] = f[i-1] + f[i-2]
    return f[N]

cnt1 = fibo(N)
cnt2 =  N-2
print(cnt1, cnt2)