string1= input("Enter a string")
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cnt=0
for i in list1:
    y=string1.count(i)
    if y>=1:
        cnt=cnt+1
if cnt>=26:
    print("pangram")
else:
    print("not pangram")
    
