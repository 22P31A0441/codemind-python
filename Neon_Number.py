n=int(input())
s=n**2
p=0
while s>0:
    r=s%10
    s=s//10
    p=p+r
if n==p:
    print("Neon Number")
else:
    print("Not Neon Number")
    