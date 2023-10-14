n=int(input())
l=list(map(int,input().split()))
s=0
r=0
for i in range(0,n):
    if i%2==0:
        s=s+l[i]
for i in range(0,n):
    if i%2!=0:
        r=r+l[i]
p=s-r
Q=r-s
if p>Q:
    print(p)
elif Q>p:
    print(Q)
elif p==Q:
    print(Q)
