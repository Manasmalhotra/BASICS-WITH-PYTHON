n=int(input())
scores=[]
names=[]
you=[]
if n in range(0,6):
    for i in range(0,n):
        name=input()
        names.append(name)
        score=float(input())
        scores.append(score)       
z=min(scores)
for i in range(0,n-1):
    if scores[i]==z:
        scores.remove(z)
        names.remove(names[i])
y=min(scores)
for i in range(0,n-1):
    if y==scores[i]:
        you.append(names[i])
x=sorted(you)
for i in range(0,len(you)):
    w=x[i]
    print(w)
