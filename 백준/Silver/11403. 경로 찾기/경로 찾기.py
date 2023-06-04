# # 플로이드 와샬
# #dfs

# n=int(input())

# graph=[]

# for i in range(n):
#     a=list(map(int,input().split()))
#     graph.append(a)
    

# def dfs(v):
    
#     for i in range(n):
#         if graph[v][i]==1 and visited[i]==0:
#             visited[i]=1
#             dfs(i)
    
    

# visited=[0 for _ in range(n)]
# for i in range(n):
#     dfs(i)
#     for j in range(n):
#         if visited[j]==1:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     visited=[0 for _ in range(n)]
#     print()


n=int(input())

graph=[]

for i in range(n):
    a=list(map(int,input().split()))
    graph.append(a)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i]==1 and graph[i][k]==1:
                graph[j][k]=1
                
for i in graph:
    for j in i:
        print(j,end=" ")
        
    print()