import math
n,m,s=map(int,input().split())
power=math.pow(n,m)
p=power%s
print(f"{p:.0f}")
