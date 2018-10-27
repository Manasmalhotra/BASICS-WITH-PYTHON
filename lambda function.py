def g(x):
    return 3*x+1
z= int(input())
print(g(z))
h=lambda y:3*y+1
q=int(input())
print(h(q))

def build_quadratic(a,b,c):
    return lambda x:a*x**2+b*x+c
f= build_quadratic(1,2,3)
print(f(9))
