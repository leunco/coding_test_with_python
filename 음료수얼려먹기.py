N, M = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x,y): # 좌표(x,y) -> (0,0)부터 시작, (N,M)보다 클 수가 없음
    if x <= -1 or x >= N or y <= -1 or y >= M: # 범위를 벗어나면 False로 처리
        return False

    if graph[x][y] == 0: # 방문X, 1은 방문했음을 표시
        graph[x][y] = 1

        dfs(x, y+1) # 상
        dfs(x, y-1) # 하
        dfs(x-1, y) # 좌
        dfs(x+1, y) # 우
        return True

    return False

res = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            res += 1

print(res)