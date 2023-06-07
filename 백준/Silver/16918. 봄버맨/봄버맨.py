from collections import deque

# 폭탄이 모두 폭발한다.
def bfs(q,graph):
    while q:
        x,y = q.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if -1<nx<R  and -1<ny<C and graph[nx][ny] =='O':
                graph[nx][ny] = '.'

def simul(t):
    global q, graph
    if t == 1:
        for i in range(R):
            for j in range(C):
                if graph[i][j] == 'O':
                    q.append((i,j))
    elif t%2==1:
        bfs(q,graph)
        for i in range(R):
            for j in range(C):
                if graph[i][j]=='O':
                    q.append((i,j))
                    
    else:
        graph=[['O']*C for _ in range(R)]


R,C,N=map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]
graph=[]
for i in range(R):
    a=list(list(input().rstrip()))
    graph.append(a)
    

q=deque()


for i in range(1,N+1):
    simul(i)
    
for i in graph:
    print(''.join(i))