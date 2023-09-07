n=input()
len_n=len(n)
n=int(n)
copy_n=n
s=0
i=len_n
while n!=0:
    r=n%10
    s=s+(r**i)
    n=n//10
    i=i-1
if(s==copy_n):
    print("True")
else:
    print("False")