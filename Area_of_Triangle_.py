a,b,c=map(int,input().split())
s=(a+b+c)*0.5
d=(s*(s-a)*(s-b)*(s-c))**0.5
print(f"{d:.2f}")
