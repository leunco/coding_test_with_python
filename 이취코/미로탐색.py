from collections import deque

N, M = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우 이동 방향 결정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y): # (x,y) 좌표
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4): # 이동 결정
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M: # 범위를 벗어나면 패스
                continue
            if graph[nx][ny] == 0: # 못 가는 곳이면 패스
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1 # 방문경로의 길이값으로 graph 대체
                queue.append((nx,ny)) # 이동한 (nx,ny) 좌표를 queue에 넣어서 모든 경로를 다 파악할 수 있도록

    return graph[N-1][M-1] # 최종 (N-1,M-1) 좌표에 대체된 값(방문경로 길이)을 리턴

print(bfs(0,0))

