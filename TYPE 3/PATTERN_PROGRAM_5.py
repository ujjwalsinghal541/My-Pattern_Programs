H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
54321
5432
543
54
5
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(N,i-1,-1):
        print(j,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
