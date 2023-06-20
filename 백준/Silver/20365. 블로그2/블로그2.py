n=int(input())
col=input()

colors={"B":0,"R":0}

colors[col[0]]+=1

for i in range(1,n):
    if col[i]!=col[i-1]:
        colors[col[i]]+=1


r=min(colors['B'],colors['R'])+1
print(r)
