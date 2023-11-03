r,c=map(int,input().split())
mat=[]
s=0
a=0
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
for t in range(r):
    for j in range(c):
        if t%2==0:
            s=s+mat[t][j]
        else:
            a=a+mat[t][j]
print(s,a)