# PRACT 05: INVERSE MATRIX
# Q1 WAPP TO INPUT MATRIX AND DISPLAY DETERMINANT AND INVERSE OF THAT MATRIX.
# Q2 WAPP TO FIND EIGEN VALUE AND EIGEN VECTORS OF MATRIX A.



import numpy as np
m=int(input("Enter the no of rows in matrices A & B:"))
n=int(input("Enter the no of Column in matrices A & B:"))
M=[]
for i in range(0,m):
    M.append([])
    M[i]=[0]*n
    for j in range(0,n):
        print("Entry of Matrix M[",i+1,",",j+1,"]=")
        M[i][j]=int(input())
print("Matrix M :\n", np.mat(M))
a=np.linalg.det(M)
print("Determinant of matrix M is:",a)
if a!=0:
    Minv=np.linalg.inv(M)
    print("The inverse of matrix M is:\n",np.mat(Minv))
else:
    print("Matrix is not Invertible")


A=np.mat("1,-1,0;-1,2,-1;0,-1,1")
def eigen(A):
    import numpy as np
    print("A:\n",A)
    e_values, e_vectors=np.linalg.eig(A)
    print("\n eigen values are: \n", e_values)
    print("\n eigen vectors are: \n", e_vectors)
