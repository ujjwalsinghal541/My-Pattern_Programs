H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    E
   E D
  E D C
 E D C B
E D C B A
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0

for i in range(N,0,-1):
    for j in range(N,N-i+1,-1):
        print(' ',end="")
    for j in range(N,i-1,-1):
        A=chr(j+64)
        print(A,end=' ')
    print("\n")
    
input("PRESS ENTER TO EXIT")
