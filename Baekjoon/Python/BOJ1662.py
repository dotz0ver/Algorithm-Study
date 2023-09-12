import sys
input = sys.stdin.readline

S = input().strip()
stack = []

for i in range(len(S)):
    if S[i] == "(":
        stack.append("(")
    elif S[i] == ")":
        cnt = 0
        while True:
            tmp = stack.pop()
            if tmp == "(":
                break
            cnt += tmp
        stack.append(int(stack.pop()) * cnt)
    elif i < len(S) - 1 and S[i + 1] == "(":
        stack.append(int(S[i]))
    else:
        stack.append(1)

result = 0
for st in stack:
    result += st
print(result)