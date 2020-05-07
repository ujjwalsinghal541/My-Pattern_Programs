H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    A
   BB
  CCC
 DDDD
EEEEE
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(N-i,0,-1):
            print(' ',end='')
    for j in range(i,2*i):
            print(j,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
