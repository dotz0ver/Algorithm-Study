import sys
input = sys.stdin.readline

def getMaxPurchases(n, b, a, n_price):
    end = 0
    start = 0
    for i in range(a):
        b -= n_price[i] // 2
        end = i + 1
        if b < 0:
            return i
    while end < n:
        if end - start < a:
            b -= n_price[end] // 2
            if b < 0:
                break
            end += 1
        else:
            if a > 0:
                b -= n_price[start] //2
                start += 1
            else:
                b -= n_price[end]
                if b < 0:
                    break
                end += 1
    return end

n, b, a = map(int, input().split())
n_price = list(map(int, input().split()))
n_price.sort()

result = getMaxPurchases(n, b, a, n_price)
print(result)