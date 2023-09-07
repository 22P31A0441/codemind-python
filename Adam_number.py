n=int(input())
sq=n*n
rev=0
reve=0
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
sqq=rev*rev
while sqq>0:
    re=sqq%10
    sqq=sqq//10
    reve=reve*10+re
if(reve==sq):
    print("True")
else:
    print("False")
    