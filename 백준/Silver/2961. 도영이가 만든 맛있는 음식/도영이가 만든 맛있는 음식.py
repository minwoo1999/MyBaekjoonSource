from itertools import combinations
n=int(input())

sour=[] # 신맛
bitter=[] # 쓴맛
for i in range(n):
    a,b=map(int,input().split())
    sour.append(a)
    bitter.append(b)
    

diff=int(10e9)
for i in range(1,n+1): # 1~n개를 뽑을 경우
    comb=list(combinations(list(range(n)),i))
    
    for food in comb:
        s=1
        b=0
        for k in range(i):
            s*=sour[food[k]]
            b+=bitter[food[k]]
        if abs(s-b)<diff:
            diff=abs(s-b)
            


print(diff)