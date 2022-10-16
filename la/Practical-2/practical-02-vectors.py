#Practical No:-02 Vectors
#Q1 Write a program to input two real vectors
#Q2 Write a program to input find linear combination of these two vector
#Q3 Write a program to find product of this two vectors.

n=int(input("Enter the dimension of vectors: "))
u=list()
print("Enter the value u: ")
for i in range(0,n):
    p=int(input(""))
    u.append(p)
print("Vector u is: ",u)

v=list()
print("Enter the vector: ",v)
for i in range(0,n):
    p=int(input(""))
    v.append(p)
print("vector v is: ",v)

def combine(a,b):
    c=[0]*n
    for i in range(0,n):
        c[i]=a*u[i]+b*v[i]
    return c

def product():
    s=0
    for i in range(0,n):
        s=s+u[i]*v[i]
    return s
