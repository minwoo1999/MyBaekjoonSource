# 문자열의 뒤에 A를 추가한다.
# 문자열 뒤에 B를 추가하고 문자열을 뒤집는다 즉
# S ==T 가 같아야한다.
#[::-1] 뒤집기, [:-1] 마지막꺼 제외하고 출력 ,[1:] 처음꺼 제외하고 출력

import sys
S=input()
T=input()

def dfs(t):
    if t==S:
        print(1)
        sys.exit()
        
    if len(t)==0:
        return 0
    if t[0]=="B":
        dfs(t[1:][::-1]) ## 처음이 B일경우 처음 B제거하고 뒤집어서 DFS]
        
    if t[-1]=="A": ## 마지막이 A일때
        dfs(t[:-1]) ## 마지막꺼 제외하고 dfs 돌리기


dfs(T)
print(0)