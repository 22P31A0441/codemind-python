n=int(input())
s=0
list1=list(map(int,input().split()))
for i in list1:
    if i%2==0:
        s=s+i
print(s)