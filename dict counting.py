my_list=[1,2,4,5,6,4,2,1]
count={}
for i in my_list:
    if i in count.keys():
        count[i]+=1
    else:
        count[i]=1
print(count.values())        
