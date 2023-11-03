n=int(input())
mat=[]
mat1=[]
for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)
for j in range(n):
    b=list(map(int,input().split()))
    mat1.append(b)
for r in range(n):
    for v in range(n):
        print(mat[r][v]+mat1[r][v],end=' ')
    print()