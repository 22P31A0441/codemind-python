a,b,c=map(int,input().split())
if a>b and a>c:
    if b>c:
        print(a+b)
    else:
        print(a+c)
if b>a and b>c:
    if c>b:
        print(b+c)
    else:
        print(b+a)
if c>a and c>b:
    if a>b:
        print(a+c)
    else:
        print(c+b)