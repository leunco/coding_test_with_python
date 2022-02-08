## 내 코드
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
max1, max2 = data[-1], data[-2]

_list = M * [max1]
for i in range(K,M,K+1):
    _list[i] = max2

print(sum(_list))

## 풀이 1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]  # 첫 번째로 큰 수
second = data[n - 2]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:
            break
        result += first
        m -= 1  # 수를 하나씩 더하면 m의 개수를 하나씩 줄이기

    if m == 0:
        break
    result += second
    m -= 1

print(result)

## 풀이 2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]  # 첫 번째로 큰 수
second = data[n - 2]  # 두 번째로 큰 수

# 가장 큰수가 더해지는 횟수 계산
count = int(m/ (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)
