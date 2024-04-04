def solution(n):
    n_sort = sorted(str(n), reverse=True)
    return int("".join(n_sort))