from collections import deque
def bfs(a,b):
    q=deque()
    q.append((a,b))
    temp=[]
    temp.append((a,b))

    while q:
        x,y=q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if -1<nx<N and -1<ny<N and visited[nx][ny]==0:
                if L<=abs(graph[nx][ny]-graph[x][y])<=R:
                    visited[nx][ny]=1
                    temp.append((nx,ny))
                    q.append((nx,ny))
    return temp
N,L,R=map(int,input().split())

graph=[]

for i in range(N):
    a=list(map(int,input().split()))
    graph.append(a)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=0
while 1:
    number=0
    flag=0
    visited=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                visited[i][j]=1
                country=bfs(i,j)

            if len(country)>1:
                flag=1

                number = sum([graph[x][y] for x, y in country]) // len(country)
                    


                for x,y in country:
                    graph[x][y]=number

    if flag==0:
        break
    
    result+=1

print(result)