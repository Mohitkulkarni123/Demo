a=float(input("enter marks of sub1"))
b=float(input("enter marks of sub2"))
c=float(input("enter marks of sub3"))
d=float(input("enter marks of sub4"))
f=float(input("enter marks of sub5"))
total=a+b+c+d+f/5
if total>=90:
    print("grade A") 
elif total>=80:
    print("grade B")
elif total>=70:
    print("grade c")
elif total>=60:
    print("grade D")
elif total>=50:
    print("grade e")
else:
    print("grade f")