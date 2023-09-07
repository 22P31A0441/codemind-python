n=int(input())
rev=0
for i in range(1,n+1):
    a=int(input())
    q=a
    while a>0:
        r=a%10
        a=a//10
        rev=rev*10+r
    if (rev==q):
        print("True")
    else:
        print("False")
    rev=0