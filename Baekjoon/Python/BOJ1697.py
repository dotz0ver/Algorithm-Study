import sys
from collections import deque
input = sys.stdin.readline

max = 100001
N, K = map(int, input().split())
arr = [0] * max

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(arr[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i < max and arr[i] == 0:
                arr[i] = arr[x] + 1
                q.append(i)
bfs()