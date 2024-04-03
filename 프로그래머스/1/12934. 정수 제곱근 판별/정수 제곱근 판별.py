def solution(n):
    x = int(n ** 0.5)
    if n == x ** 2:
        return (x+1) ** 2
    else:
        return -1