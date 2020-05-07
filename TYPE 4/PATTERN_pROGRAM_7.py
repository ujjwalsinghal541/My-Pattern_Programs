H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    E
   DD
  CCC
 BBBB
AAAAA
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(i-1,0,-1):
            print(' ',end='')
    for j in range(i,N+1):
            A=chr(i+64)
            print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
