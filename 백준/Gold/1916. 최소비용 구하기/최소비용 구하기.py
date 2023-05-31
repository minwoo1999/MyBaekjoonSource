def dijkstra(start):

    dist[start]=0
    q=[(start,0)]
    
    while q:
        cur,wei=heapq.heappop(q)
        
        if dist[cur]<wei:
            continue
        
        for dest,cost in graph[cur]:
            cost=cost+dist[cur]
            if dist[dest]>cost:
                dist[dest]=cost
                heapq.heappush(q,(dest,cost))

import heapq
n=int(input())
m=int(input())
INF=int(1e9)
graph=[[] for _ in range(n+1)]
for i in range(m):
    s,d,wei=map(int,input().split())
    graph[s].append((d,wei))
    
s,d=map(int,input().split())

dist=[INF]*(n+1)

dijkstra(s)
print(dist[d])