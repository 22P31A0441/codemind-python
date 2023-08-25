n=int(input())
n1=0
n2=1
s=0
for i in range(1,n-1):
    n3=n1+n2
    if n3==n:
        s=1
    n1=n2
    n2=n3
if (s==1):
    print("True")
else:
    print("False")
        