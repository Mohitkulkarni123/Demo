n=int(input("enter any digit number"))
i=0
sum=0
while n>1:
      n=n//10
      b=n%10
      sum=sum+b
print("addition is ",sum)