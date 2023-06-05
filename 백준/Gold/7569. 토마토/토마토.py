import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int,input().split())


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

data = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()

#3차원 bfs문제
def bfs():
    while q:
        # 높이, x,y 순서
        z,x,y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1<nx<n and -1<ny<m and -1<nz<h:
                # 높이, x,y 순서
                if data[nz][nx][ny] == 0:
                    data[nz][nx][ny] = data[z][x][y]+1
                    q.append((nz,nx,ny))
            
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 높이, x,y 순서
            if data[i][j][k] == 1:
                # 높이, x,y 순서
                q.append((i,j,k))
bfs()

flag=0
result=-2
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k]==0:
                flag=1
            result=max(result,data[i][j][k])


# 토마토가 익지못하는 경우
if flag==1:
    print(-1)
elif result==1:
    print(0)
else:
    print(result-1)
    