H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    A
   12
  ABC
 1234
ABCDE
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0
for i in range(1,N+1):
    for j in range(N,i,-1):
            print(' ',end='')
    for j in range(1,i+1):
            if i%2==0:
                print(j,end='')
            else:
                A=chr(64+j)
                print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
