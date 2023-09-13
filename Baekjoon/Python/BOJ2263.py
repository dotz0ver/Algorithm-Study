import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
inorder = [int(x) - 1 for x in input().split()]
postorder = [int(x) - 1 for x in input().split()]
in_pos = [0] * (n+1)
result = []

def preorder(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return
    p = postorder[post_end]

    size = in_pos[p] - in_start
    result.append(p+1)

    preorder(in_start, in_pos[p]-1, post_start, post_start+size-1)
    preorder(in_pos[p]+1, in_end, post_start+size, post_end-1)

for i in range(n):
    in_pos[inorder[i]] = i

preorder(0, n-1, 0, n-1)
print(*result)