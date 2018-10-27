string1=input("Enter a string")
y= list(string1.split())
z=set(y)
for i in z:
    w= string1.count(i)
    print("The frequency of",i,"is",w)
    
