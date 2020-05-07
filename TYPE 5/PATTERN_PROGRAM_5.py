H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    1
   2 3
  3 4 5
 4 5 6 7
5 6 7 8 9
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0

for i in range(1,N+1):
    for j in range(i,N):
        print(' ',end="")
    for j in range(i,2*i):
        print(j,end=" ")
    print("\n")
    
input("PRESS ENTER TO EXIT")
