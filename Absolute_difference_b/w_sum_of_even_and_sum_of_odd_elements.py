n=int(input())
s=0
r=0
l=list(map(int,input().split()))
for i in range(0,n):
    if l[i]%2==0:
        s=s+l[i]
for i in range(0,n):
    if l[i]%2!=0:
        r=r+l[i]
p=s-r
q=r-s
if p>q:
    print(p)
elif q>p:
    print(q)
elif p==q:
    print(p)
    
    