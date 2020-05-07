H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    5
   5 4
  5 4 3
 5 4 3 2
5 4 3 2 1
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0

for i in range(N,0,-1):
    for j in range(N,N-i+1,-1):
        print(' ',end="")
    for j in range(N,i-1,-1):
        print(j,end=' ')
    print("\n")
    
input("PRESS ENTER TO EXIT")
