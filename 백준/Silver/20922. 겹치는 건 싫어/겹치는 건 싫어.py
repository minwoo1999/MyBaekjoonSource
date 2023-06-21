n,k=map(int,input().split())

lst=list(map(int,input().split()))

left,right=0,0

count=[0]*(max(lst)+1)
answer=0
while right<n:
    
    if count[lst[right]]<k: # 같은 원소가 k보다 작게 있는경우
        count[lst[right]]+=1 ## 카운트를 늘려주고
        right+=1 ## 오른쪽으로 확장해서 찾아본다
    else:
        
        count[lst[left]]-=1 # k보다 작아질때까지 -1을 해준다
        left+=1 ## 좌측에서 계속 -를 실시

    answer=max(answer,right-left) #최장연속부분수열 구하기

print(answer)