def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if count_divisors(num) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer