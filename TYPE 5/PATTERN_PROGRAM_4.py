H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    5
   4 4
  3 3 3
 2 2 2 2
1 1 1 1 1
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(i,N):
        print(' ',end="")
    for j in range(1,i+1):
        print(i,end=" ")

    print("\n")
    
input("PRESS ENTER TO EXIT")
