#Prac 8 Title:-decomposition of vector
# Q1 WAP to check whether the given vectors are orthogonal.If yes,then check whether they are orthonormal.
# Q2 WAP to decompose vectors b as sum of vector closest to a and vector orthogonal to a.

def ips(x,y):
    p=0
    for i in range(len(x)):
        p+=x[i]*y[i]
    return p
def norm(x):
    import math as m
    nrm=m.sqrt(ips(x,x))
    return nrm
def ortho(x,y):
    if abs(ips(x,y))<=0.000000000001:
        if norm(x)==1 and norm(y)==1:
            print(x,'and',y,'are orthonormal')
        else:
            print(x,'and',y,'are orthogonal')
    else:
        print(ips(x,y))
        print(x,'and',y,'are not orthogonal')

def proj(v,u):
    t=ips(u,v)/ips(u,u)
    p=[0]*len(u)
    for i in range(len(u)):
        p[i]=t*u[i]
    return p

def Decompose(b,a):
    b1=proj(b,a)
    b2=[0]*len(b)
    for i in range(len(b)):
        b2[i]=b[i]-b1[i]
    print(b,'=',b1,'+',b2)