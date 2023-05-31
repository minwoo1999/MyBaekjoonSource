n=int(input())

dic_word=[]
dic_list={'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
result=[]
for i in range(n):
    a=input()
    dic_word.append(a)


for alph in dic_word:
    for i in range(len(alph)):
        num=10**(len(alph)-i-1)
        dic_list[alph[i]]+=num



for i in dic_list.values():
    if i>0:
        result.append(i)


result.sort(reverse=True)
answer=0
for i in range(len(result)):
    answer+=(9-i)*result[i]

print(answer)
