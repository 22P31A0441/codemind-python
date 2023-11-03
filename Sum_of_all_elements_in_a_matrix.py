r,c=map(int,input().split())
mat=[]
for i in range(r):
    l_i=list(map(int,input().split()))
    mat.append(l_i)
s=0
for l_i in mat:
    for j in l_i:
        s=s+j
print(s)