H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    A
   CB
  EDC
 GFED
IHGFE
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(N,i,-1):
            print(' ',end='')
    for j in range(2*i-1,i-1,-1):
            A=chr(j+64)
            print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
