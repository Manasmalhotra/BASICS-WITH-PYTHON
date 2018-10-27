x=int(input("enter a number "))
y=0
c=x
while x>0:
    r= int(x%10)
    y= (10*y)+r
    x= int(x/10)
print("Reverse of the number is: ",y)
if c==y:
    print("The number is a palindrome number")
