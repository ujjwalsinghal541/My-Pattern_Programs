H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    1
   22
  333
 4444
55555
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,N-i+1):
            print(' ',end='')
    for j in range(N-i+1,N+1):
            print(i,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
