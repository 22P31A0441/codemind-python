n=int(input())
list1=list(map(int,input().split()))
avg=sum(list1)
s=avg//n
print(s in list1)