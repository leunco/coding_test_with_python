## 백준 1931 회의실배정
## 정렬, 그리디
N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data.sort(key = lambda x:(x[1],x[0])) # 중요!!

cnt = 1
x = data[0][1] # 끝
for i in range(1,N):
    if x <= data[i][0]: # 시작(data[i][0])과 끝을 비교
        cnt += 1        # 다음 시작이 끝보다 크거나 같으면 다음 회의로 넘어갈 수 있음
        x = data[i][1] # 끝

print(cnt)
