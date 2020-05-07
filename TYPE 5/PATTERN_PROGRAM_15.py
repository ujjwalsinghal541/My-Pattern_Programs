H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    E
   D D
  C C C
 B B B B
A A A A A
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0

for i in range(N,0,-1):
    for j in range(N,N-i+1,-1):
        print(' ',end="")
    for j in range(N,i-1,-1):
        A=chr(i+64)
        print(A,end=' ')
    print("\n")
    
input("PRESS ENTER TO EXIT")
