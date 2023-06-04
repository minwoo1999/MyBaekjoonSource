n=int(input())
graph=[]
visited=[0 for _ in range(n)]
for i in range(n):
    a=list(map(int,input().split()))
    graph.append(a)


def dfs(v):

    for i in range(n):
        if graph[v][i]==1 and visited[i]==0:
            visited[i]=1
            dfs(i)


for i in range(n):
    dfs(i)

    for j in range(n):
        if visited[j]==1:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
    visited=[0 for _ in range(n)]
    
        

