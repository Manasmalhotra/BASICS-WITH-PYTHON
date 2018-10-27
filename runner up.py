my_list=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    my_list.append(x)
my_list.sort(reverse=True)
print(my_list[1])
