import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(t):
    global cnt
    visited[t] = cnt
    graph[t].sort()
    for i in graph[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
dfs(R)

for i in range(1, N+1):
    print(visited[i])




