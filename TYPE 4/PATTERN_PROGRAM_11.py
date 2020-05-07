H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    1
   2 3
  4 5 6
 7 8 9 10
11 12 13 14 15
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0
for i in range(1,N+1):
    for j in range(N,i,-1):
            print(' ',end='')
    for j in range(2*i-1,i-1,-1):
            A=A+1
            print(A ,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
