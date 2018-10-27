n=int(input("enter a number"))
a=-1
b=1
for i in range(0,n+1):
    c= a+b
    print(c)
    a=b
    b=c
input("Press enter to exit")    
