import math

def isPrime(num):
    
    if num==0 or num==1:
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
            
    
    return True
            
            
    
    

n=int(input())

result=[]
for i in range(n):
    a=int(input())
    while(1):
        if isPrime(a):
            result.append(a)
            break
        else:
            a+=1
            

for i in result:
    print(i)
        
        

