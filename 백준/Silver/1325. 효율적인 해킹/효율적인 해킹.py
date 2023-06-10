from collections import deque
def bfs(start):
    visited=[False for _ in range(n+1)]
    visited[start]=True
    cnt=1

    q=deque()
    q.append(start)

    while q:
        cur=q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                visited[i]=True
                cnt+=1
                q.append(i)

    return cnt
    

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)

Maxcnt=0
result=[]
for i in range(1,n+1):
    cnt=bfs(i) # 1부터 탐색 시작

    if cnt>Maxcnt:
        Maxcnt=cnt
        result.clear()
        result.append(i)
    elif cnt==Maxcnt:
        result.append(i)



result.sort()
for i in result:
    print(i,end=" ")

