import sys
a,b=map(int,sys.stdin.readline().split())

rank=[]
for i in range(a):
    tmp=input().split()
    tmp[1]=int(tmp[1])
    rank.append(tmp)



for i in range(b):

    n=int(sys.stdin.readline())
    left,right=0,a-1
    mid=(left+right)//2

    while left<=right:
        if n>rank[mid][1]:
            left=mid+1
        else:
            right=mid-1
        mid=int(right+left)//2

    mid=left
    print(rank[mid][0])
