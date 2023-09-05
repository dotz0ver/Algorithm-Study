import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        Y, X = map(int, input().split())
        graph[X][Y] = 1

    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1:
                dfs(x, y)
                cnt += 1

    print(cnt)