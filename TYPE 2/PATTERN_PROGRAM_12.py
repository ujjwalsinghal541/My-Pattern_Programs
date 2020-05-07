H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
A
BC
CDE
DEFG
EFGHI
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(i,2*i):
        A=chr(j+64)
        print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
