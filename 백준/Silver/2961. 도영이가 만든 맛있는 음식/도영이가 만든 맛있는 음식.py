from itertools import combinations
n=int(input())


arr=[]
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)
    

comb=[]
for i in range(1,n+1):
    comb.append(combinations(arr,i))
    
answer=int(10e9)    
for i in comb:
    for j in i:
        s=1
        b=0
        for k in j:
            s*=k[0]
            b+=k[1]
        answer=min(answer,abs(s-b))
        


print(answer)