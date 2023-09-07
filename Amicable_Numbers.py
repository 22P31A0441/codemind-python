n=int(input())
m=int(input())
s=0
r=0
for i in range(1,n):
  if n%i==0:
     s=s+i
for i in range(1,m):
  if m%i==0:
     r=r+i
if(s==m and r==n):
    print("Amicable")
else:
    print("Not Amicable")