H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    5
   4 4
  3 3 3
 2 2 2 2
1 1 1 1 1
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0

for i in range(N,0,-1):
    for j in range(N,N-i+1,-1):
        print(' ',end="")
    for j in range(i,N+1):
        print(i,end=' ')
    print("\n")
    
input("PRESS ENTER TO EXIT")
