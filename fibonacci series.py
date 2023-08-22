n=int(input("enter a number:"))
prev=0
next=1
print(prev,next,end='')
i=1
while i<n:
      r=prev+next
      print(r)
      prev=next 
      next=r
      i=i+1
