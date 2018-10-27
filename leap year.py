z=int(input("enter a number"))
result= "leap year" if z%400==0 else "leap year" if z%4==0 and z%100!=0 else "not a leap year"
print(result)
