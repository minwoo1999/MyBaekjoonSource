from collections import deque

def wall_Check(i, j):
    for x, y in wall:
        if i <= x < i + H and j <= y < j + W:
            return False
    return True

def bfs():
    q = deque()
    q.append((Sr-1, Sc-1, 0))
    
    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = True
        if x == Fr-1 and y == Fc-1:
            print(cnt)
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 

            if wall_Check(nx, ny): # 직사각형 안에 벽이 없고
                if 0 <= nx < N and 0 <= ny < M and 0 <= nx + H - 1 < N and 0 <= ny + W - 1 < M:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, cnt + 1))

    print(-1)
    return

N, M = map(int, input().split())

graph = []

for _ in range(N):
    a = list(map(int, input().split()))
    graph.append(a)

H, W, Sr, Sc, Fr, Fc = map(int, input().split())

wall = []
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽 저장
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            wall.append((i, j))

bfs()
