from collections import deque

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())

for _ in range(T):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    visited = [[0] * l for _ in range(l)]

    queue = deque()
    queue.append((x1, y1))
    visited[x1][y1] = 1

    while queue:
        x, y = queue.popleft()

        if x == x2 and y == y2:
            print(visited[x][y] - 1)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))