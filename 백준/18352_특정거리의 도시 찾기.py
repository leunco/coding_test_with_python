## 백준 18352 : 특정 거리의 도시 찾기
import sys
from collections import deque

input = sys.stdin.readline
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0 # 출발도시 -> 출발도시 거리 0

q = deque([x]) # 출발지점 큐에 넣기

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1: # 방문 안함
            distance[next_node] = distance[now] + 1 # 최단 거리 갱신
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False: # 최단 거리가 k인 도시가 없으면 -1 출력
    print(-1)

