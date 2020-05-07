H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    E
   DD
  CCC
 BBBB
AAAAA
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(N-i,0,-1):
            print(' ',end='')
    for j in range(2*i-1,i-1,-1):
            print(j,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
