lis = list(map(int,input().strip().split()))[:4]
x1=int(lis[0])
x2=int(lis[1])
v1=int(lis[2])
v2=int(lis[3])
count=0
c=0
for n in range(0,1000):
   if((x1+v1)==n*(x2+v2) or n*(x1+v1)==(x2+v2)):
      c=c+1
      break
   else:
      count+=1
if(count==1):
    print("NO")
else:
    print("YES")
