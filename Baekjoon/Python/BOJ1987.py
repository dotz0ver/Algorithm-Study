import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [0] * 26

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
Max = 0

def dfs(x, y, cnt):
    global Max
    if Max < cnt:
        Max = cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx<R and nx>=0 and ny<C and ny>=0 and visited[ord(arr[nx][ny])-65] == 0:
            visited[ord(arr[nx][ny])-65] = 1
            dfs(nx, ny, cnt+1)
            visited[ord(arr[nx][ny])-65] = 0
Max = 1
visited[ord(arr[0][0])-65] = 1
dfs(0, 0, Max)
print(Max)