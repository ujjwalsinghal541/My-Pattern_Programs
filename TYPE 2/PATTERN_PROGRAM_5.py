H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
5
54
543
5432
54321
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(N,N-i,-1):
        print(j,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
