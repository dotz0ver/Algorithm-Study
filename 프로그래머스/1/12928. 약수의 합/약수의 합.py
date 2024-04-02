def solution(n):
    nList = []
    for i in range(1, n + 1):
        if (n % i == 0) :
            nList.append(i)
    answer = sum(nList) 
    return answer