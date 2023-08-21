b=int(input("enter salary of employee"))
if b<=10000:
    hra=b*0.2
    da=b*0.8
    c=hra+da
    print(c)
elif b<=20000:
     hra=b*0.25
     da=b*0.9
     d=hra+da
     print(d)
elif b>20000:
     hra=b*0.3
     da=b*0.95
     e=hra+da
     print(e)

