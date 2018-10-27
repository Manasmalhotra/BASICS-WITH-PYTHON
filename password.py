x=input("enter password")
count=0
string="abcdefghijklmnopqrstuvwxyz"
string2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string3="0123456789"
string4="$@#"
for i in x:
    if i in string:
        count=count+1
        break 
for i in x:
    if i in string2:
        count=count+1
        break
for i in x:
    if i in string3:
        count=count+1
        break
for i in x:
    if i in string4:
        count=count+1
        break
if len(x)>6 and len(x)<16:
    count=count+1
if count==5:
    print("valid")
else:
    print("not valid")
