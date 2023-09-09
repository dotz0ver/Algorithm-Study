import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
coin = 0
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)

for i in arr:
    coin += K//i
    K = K % i
print(coin)