x= int(input("enter a number"))
sum=0
while x>0:
    r= int(x%10)
    sum= sum+r
    x=int(x/10)
print(sum)    
