n=int(input())
a=len(str(n))
sq=n**2
b=sq%(10**a)
if b==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")