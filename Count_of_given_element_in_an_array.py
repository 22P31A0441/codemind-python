n=int(input())
c=0
l=list(map(int,input().split()))
m=int(input())
for i in range(0,len(l)):
    if m==l[i]:
        c=c+1
print(c)