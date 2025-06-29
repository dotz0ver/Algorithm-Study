import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
plane = []
for _ in range(P):
    plane.append(int(input()))

count = 0
for p in plane:
    x = find(p)
    if x == 0:
        break
    union(x, x-1)
    count += 1

print(count)