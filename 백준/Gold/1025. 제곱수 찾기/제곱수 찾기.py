from math import sqrt

n,m=map(int,input().split())

graph=[]

for i in range(n):
    a=input()
    graph.append(a)

result=-1

for i in range(n):
    for j in range(m):
        for k in range(-n,n):
            for l in range(-m,m):
                if k==0 and l ==0:
                    continue
                x=i
                y=j
                temp=''
                while 0<=x<n and 0<=y<m:
                    temp+=graph[x][y]
                    if int(temp) == int(int(temp)**0.5)**2:
                        result=max(result,int(temp))
                    x+=k
                    y+=l



print(result)

                
