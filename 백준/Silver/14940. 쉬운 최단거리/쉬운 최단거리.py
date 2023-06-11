from collections import deque

def bfs():

    while q:
        x,y=q.popleft()
        visited[x][y]=1

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if -1<nx<n and -1<ny<m and visited[nx][ny]==0 and graph[nx][ny]==1:
                q.append((nx,ny))
                visited[nx][ny]=1
                graph[nx][ny]=graph[x][y]+1




n,m=map(int,input().split())


graph=[]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    a=list(map(int,input().split()))
    graph.append(a)

q=deque()


for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            graph[i][j]=0
            q.append((i,j))
            break



bfs()

for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and graph[i][j]==1:
            graph[i][j]=-1


for i in range(n):
    for j in range(m):
        print(graph[i][j],end=" ")


    print()
