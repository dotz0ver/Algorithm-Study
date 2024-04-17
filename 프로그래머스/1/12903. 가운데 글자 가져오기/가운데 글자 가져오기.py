def solution(s):
    if len(s) % 2 == 0:
        idx = len(s)//2
        answer = s[idx-1:idx+1]
    else:
        idx = len(s)//2
        answer = s[idx]
    return answer