H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    A
   BC
  DEF
 GHIJ
KLMNO
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0
for i in range(1,N+1):
    for j in range(N,i,-1):
            print(' ',end='')
    for j in range(2*i-1,i-1,-1):
            A=A+1
            B=chr(A+64)
            print(B,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
