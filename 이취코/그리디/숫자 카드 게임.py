## 내 코드
N, M = map(int, input().split())
data = []
for _ in range(N):
    _list = list(map(int, input().split()))
    data.append(min(_list))

print(max(data))

## 풀이 1
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

## 풀이 2
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
