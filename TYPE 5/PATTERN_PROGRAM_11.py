H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    A
   1 2
  A B C
 1 2 3 4
A B C D E
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0

for i in range(1,N+1):
    for j in range(i,N):
        print(' ',end="")
    for j in range(1,i+1):
        if i%2==0:
            print(j,end=' ')
        else:
            A=chr(j+64)
            print(A,end=' ')
    print("\n")
    
input("PRESS ENTER TO EXIT")
