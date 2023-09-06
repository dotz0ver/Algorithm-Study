import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(H)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
hx = [-2, -1, 1, 2, 2, 1, -1, -2]
hy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(n):
    q = deque()
    q.append((0, 0, n))
    check = [[[0] * (n+1) for _ in range(W)] for _ in range(H)]
    while q:
        x, y, K = q.popleft()
        if x == H-1 and y == W-1:
           return check[x][y][K]
        if K > 0:
            for i in range(8):
                nx, ny = x + hx[i], y + hy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] != 1 and check[nx][ny][K-1] == 0:
                        check[nx][ny][K-1] = check[x][y][K] + 1
                        q.append((nx, ny, K-1))
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if 0 <= nx < H and 0 <= ny < W:
                if arr[nx][ny] != 1 and check[nx][ny][K] == 0:
                    check[nx][ny][K] = check[x][y][K] + 1
                    q.append((nx, ny, K))
    return -1
print(bfs(K))