n=int(input())
rev=0
if n>0:
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    print(rev)
else:
    x=abs(n)
    while x:
        r=x%10
        x=x//10
        rev=rev*10+r
    print(-rev)