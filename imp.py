y=float(input())
x=float(input())
z= (y-x)-0.50
if x%5==0 and x<y and 0<x<=2000 and 0<=y<2000:
    print(z)
elif x%5!=0 and 0<x<=2000 and 0<=y<2000 :
    print(y)
    
elif x>y and 0<x<=2000 and 0<=y<2000:
    print(y)
    
input("Press enter to exit") 
