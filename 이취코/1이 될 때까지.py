## 내 코드
N, K = map(int, input().split())
cnt = 0

while N > 1:
    if N % K == 0:
        N = N//K
    else:
        N -= 1
    cnt += 1

print(cnt)

## 풀이 1
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

## 풀이 2
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n-target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)
