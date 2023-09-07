n=int(input())
sq=n*n
a=len(str(n))
q=sq%(10**a)
if(n==q):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")