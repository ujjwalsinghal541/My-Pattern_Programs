H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
EDCBA
EDBC
EDC
ED
E
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(N,N-i,-1):
        A=chr(j+64)
        print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
