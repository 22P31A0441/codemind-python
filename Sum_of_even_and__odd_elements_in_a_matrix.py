r,c=map(int,input().split())
mat=[]
s=0
p=0
for i in range(r):
    y=list(map(int,input().split()))
    mat.append(y)
for a in range(r):
    for b in range(c):
        if (mat[a][b])%2==0:
            s=s+mat[a][b]
        else:
            p=p+mat[a][b]
print(s,p)