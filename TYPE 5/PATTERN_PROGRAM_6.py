H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    1
   3 2
  5 4 3
 7 6 5 4
9 8 7 6 5
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0

for i in range(1,N+1):
    for j in range(i,N):
        print(' ',end="")
    for j in range(2*i-1,i-1,-1):
        print(j,end=" ")
    print("\n")
    
input("PRESS ENTER TO EXIT")
