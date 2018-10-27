z=input()
my_list=[]
my_list1=[]
w=list(z)
e=z.split(':')
for i in range(00,60):
    if i in range(0,10):
        z= "0"+str(i)+"PM"
        my_list.append(z)
    else:
        z= str(i)+"PM"
        my_list.append(z)
for i in range(00,60):
    if i in range(0,10):
        z= "0"+str(i)+"AM"
        my_list1.append(z)
    else:
        z= str(i)+"AM"
        my_list.append(z)        
for i in w:
  if int(e[0]) in range(1,13) and int(e[1])in range(0,60):
      if e[2] in my_list or e[2] in my_list1:
              if 'P' in w and e[0]!='12':
               e[0]=str(int(e[0])+12)
               c=":".join(e)
               x=list(c)
               x.remove('P')
               x.remove('M')
               print("".join(x))
               break
              elif 'A' in w and e[0]=='12':
                  e[0]='00'
                  c=":".join(e)
                  x=list(c)
                  x.remove('A')
                  x.remove('M')
                  print("".join(x))
                  break
           
              elif 'A' in w:
                   c=":".join(e)
                   x=list(c)
                   x.remove('A')
                   x.remove('M')
                   print("".join(x))
                   break
              elif 'P' in w and e[0]=='12':
                   c=":".join(e)
                   x=list(c)
                   x.remove('P')
                   x.remove('M')
                   print("".join(x))
                   break 
                
              
            
            
       
             
      
      
   
      
