def dfs(n):
    if visited[n]==False:
        visited[n]=True

        for i in arr[n]:
            up.add(n)
            down.add(i)

            if up==down: ## 순서는 다르지만 동일한 요소를 가지고 있다면 ?
                ans.extend(list(down))
                return
            dfs(i)

    

n=int(input())

arr=[[]for _ in range(n+1)]
ans=[]

for i in range(1,n+1):
    a=int(input())
    arr[i].append(a)


for i in range(1,n+1):
    visited=[False]*(n+1)

    up=set()
    down=set()

    dfs(i)

ans=list(set(ans))
ans.sort()
print(len(ans))

for i in ans:
    print(i)