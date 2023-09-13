import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

def dfs(t):
    if t == S:
        return 1
    if len(t) == 0:
        return 0
    result = 0
    if t[-1] == 'A':
        result = dfs(t[:-1])
    if t[0] == 'B':
        result = max(result, dfs(t[1:][::-1]))
    return result
result = 1 if dfs(T) else 0
print(result)