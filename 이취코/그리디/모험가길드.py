## 모험가 길드
# 내 코드
n = int(input())
group = list(map(int, input().split()))

group.sort(reverse=True) # 정렬
print(group)

start = 0
_max = group[0]
end = start+_max -1
cnt = 1

while True:
    start = end + 1
    _max = group[_max]
    end = start+_max -1

    if end >= n:
        break
    else:
        cnt+=1

print(cnt)

# 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)