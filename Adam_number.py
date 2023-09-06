n=int(input())
rem=0
reve=0
sq=n*n
q=n
while n>0:
    r=n%10
    rem=rem*10+r
    n=n//10
sqq=rem*rem
while sqq>0:
    re=sqq%10
    sqq=sqq//10
    reve=reve*10+re
if reve==sq:
    print("True")
else:
    print("False")