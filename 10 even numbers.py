n=int(input("enter numbers"))
i=1
sum=0
count=0
if n<=20:
    print("number must be greater than 20")
else:
    while i<=n and count<10: 
     if i%2==0:
      sum=sum+i
      count=count+1
    i=i+1
print("addition is",sum) 
