H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
ABCDE
FGHI
JKL
MN
P
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0
for i in range(N,0,-1):
    for j in range(i,0,-1):
        A=A+1
        B=chr(A+64)
        print(B,end=' ')
    print("\n")
    
input("PRESS ENTER TO EXIT")
