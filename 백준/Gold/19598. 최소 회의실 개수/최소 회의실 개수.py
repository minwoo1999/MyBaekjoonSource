import heapq 
n=int(input())

lst=[]

for i in range(n):
    start,end=map(int,input().split())
    lst.append((start,end))
    

# 0번인덱스 기준으로 정렬하기~
lst.sort(key=lambda x:x[0])


p=[0]
cnt=0
for start,end in lst:
    #끝나는시간보다 시작시간이 같거나 클 경우 cnt+=1
    if start>=p[0]:
        heapq.heappop(p)
    else:
        cnt+=1
        
    heapq.heappush(p,end)
    
print(cnt+1)