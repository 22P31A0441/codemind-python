a,b,c,d,e=map(int,input().split())
f=a+b+c+d+e
s=f//5
if s>=90:
    print("Grade A")
elif s>=80:
      print("Grade B")
elif s>=70:
      print("Grade C")
elif s>=60:
      print("Grade D")
elif s>=40:
      print("Grade E")
elif s<40:
      print("Grade F")