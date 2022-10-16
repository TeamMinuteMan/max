#Practical No 3 Title:- Matrix
# write a python program program to input two matrices.
# write a python program to add two matrices.
# write a python program to find scalar multiplication of matrix.
# write a python program to find transpose of matrix.
# write a python program to display specific row and column. 

m=int(input("Enter the number of rows in matrices A & B : "))
n=int(input("Enter the number of columns in matrices A & B : "))
A=[]
for i in range(0,m):
    A.append([])
    A[i]=[0]*n
    for j in range(0,n):
        print("Entry of matrix A[",i+1,",",j+1,"]=")
        A[i][j]=int(input())
print("Matrix A : ")
for i in range(0,m):
    print(A[i])
print(A)

B=[]
for i in range(0,m):
    B.append([])
    B[i]=[0]*n
    for j in range(0,n):
        print("Entry of matrix B[",i+1,",",j+1,"]=")
        B[i][j]=int(input())
print("Matrix B : ")
for i in range(0,m):
    print(B[i])
print(B)

def AddMat(A,B):
    C=[]
    for i in range(0,m):
        C.append([])
        C[i]=[0]*n
        for j in range(0,n):
            C[i][j]=A[i][j]+B[i][j]
    print("Matrix A + B : ")
    for i in range(0,m):
        print(C[i])
    print(C)

def ScaleMult(A,k):
    C=[]
    for i in range(0,m):
        C.append([])
        C[i]=[0]*n
        for j in range(0,n):
            C[i][j]=A[i][j]*k
    print("Matrix kA : ")
    for i in range(0,m):
        print(C[i])
    print(C)

def TransMat(A):
    C=[]
    for i in range(0,m):
        C.append([])
        C[i]=[0]*n
        for j in range(0,n):
            C[i][j]=A[i][j]
    print("Transpose of  Matrix : ")
    for i in range(0,m):
        print(C[i])
    print(C)

def DisRow(A,r):
    return A[r-1]

def DisCol(A,c):
    for i in range(0,n):
        print([A[i][c-1]])

def PrintCol(A,c):
    return DisRow(TransMat (A),c)
        
        










