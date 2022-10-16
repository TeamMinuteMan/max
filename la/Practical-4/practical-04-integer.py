# PRACT 04: Title:-INTEGER
# Q1 WAPP TO FIND A AND B SUCH THAT N=a^2-b^2 for N>5
# Q2 WAPP TO FIND GCD +OF TWO INTEGERS.
# Q3 WAPP TO FIND LCM OF TWO INTEGERS.



def numbers(N):
    x=1
    for i in range(2,int(N/2)):
        if N%i==0:
# M2 : N%2==0 x=2 don't use break
            x=i
            y=N/i
            a,b=(x+y)*0.5,(x-y)*0.5
            break

        else:
            a=(N-1)/2
            b=a+1
    if abs(a)<abs(b):
        a,b=b,a
    print("Value of a:",abs(a))
    print("Value of b:",abs(b))
    print("Value of N:",abs(a*a-b*b))


# Q2:
def GCD(a,b):
    x=abs(a)
    y=abs(b)
    r=1
    if x>y:
        x,y=y,x
    if y==0:
        if x==0:
            print("GCD of",a,"&",b,"is not define")
        else:
            print("GCD of",a,"&",b,"is",x)
    else:
        while r!=0:
            r=x%y
            x=y
            y=r
    return x

# Q3:
def LCM(a,b):
    print("LCM",a,"&",b,"is",(a*b)/GCD(a,b))
    

