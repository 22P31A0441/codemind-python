p,r,t=map(int,input().split())
i=(1+(r/100))**t
ci=p*i
print(f"{ci:.2f}")