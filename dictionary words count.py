string1=input("enter a string")
z=string1.split()
count={}
for i in z:
    if i in count.keys():
        count[i]+=1
    else:
        count[i]=1
print(count)
print("frequency of each word are",count.values())
