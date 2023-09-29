import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]

friends = [[0] * N for _ in range(N)]

for k in range(N):
  for i in range(N):
    for j in range(N):
      if i == j:
        continue
      # 2-친구인 경우
      if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
        friends[i][j] = 1

res = 0

for cnt in friends:
  res = max(res,sum(cnt))
print(res)